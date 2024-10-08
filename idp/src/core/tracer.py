import logging

from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.semconv.resource import ResourceAttributes

from .settings import JaegerSettings

logger = logging.getLogger(__name__)


def configure_tracer(app: FastAPI) -> None:
    settings = JaegerSettings()  # type: ignore
    if not settings.enable_tracer:
        return

    logger.warn(f"Connecting Jaeger to {settings.host}:{settings.port}")
    tracer = TracerProvider(resource=Resource({ResourceAttributes.SERVICE_NAME: "idp-api"}))
    trace.set_tracer_provider(tracer)
    tracer.add_span_processor(
        BatchSpanProcessor(
            JaegerExporter(
                agent_host_name=settings.host,
                agent_port=settings.port,
            )
        )
    )
    # Чтобы видеть трейсы в консоли
    # trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

    FastAPIInstrumentor.instrument_app(app)
