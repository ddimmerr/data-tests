from sqlmesh.core.config import Config, GatewayConfig, ModelDefaultsConfig
from sqlmesh.core.config.connection import BigQueryConnectionConfig

config = Config(
    gateways={
        "bigquery": GatewayConfig(
            connection=BigQueryConnectionConfig(
                project="data-platform-dev-509512",
                # uses your local gcloud ADC credentials
            )
        )
    },
    default_gateway="bigquery",
    model_defaults=ModelDefaultsConfig(dialect="bigquery"),
)