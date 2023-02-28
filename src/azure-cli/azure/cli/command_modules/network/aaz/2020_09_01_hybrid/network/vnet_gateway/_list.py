# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network vnet-gateway list",
)
class List(AAZCommand):
    """List virtual network gateways.

    :example: List virtual network gateways in a resource group.
        az network vnet-gateway list -g MyResourceGroup
    """

    _aaz_info = {
        "version": "2018-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/virtualnetworkgateways", "2018-11-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.VirtualNetworkGatewaysList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class VirtualNetworkGatewaysList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2018-11-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZStrType()
            _element.id = AAZStrType()
            _element.location = AAZStrType()
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.active_active = AAZBoolType(
                serialized_name="activeActive",
            )
            properties.bgp_settings = AAZObjectType(
                serialized_name="bgpSettings",
            )
            properties.enable_bgp = AAZBoolType(
                serialized_name="enableBgp",
            )
            properties.gateway_default_site = AAZObjectType(
                serialized_name="gatewayDefaultSite",
            )
            _ListHelper._build_schema_sub_resource_read(properties.gateway_default_site)
            properties.gateway_type = AAZStrType(
                serialized_name="gatewayType",
            )
            properties.ip_configurations = AAZListType(
                serialized_name="ipConfigurations",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
            )
            properties.sku = AAZObjectType()
            properties.vpn_client_configuration = AAZObjectType(
                serialized_name="vpnClientConfiguration",
            )
            properties.vpn_type = AAZStrType(
                serialized_name="vpnType",
            )

            bgp_settings = cls._schema_on_200.value.Element.properties.bgp_settings
            bgp_settings.asn = AAZIntType()
            bgp_settings.bgp_peering_address = AAZStrType(
                serialized_name="bgpPeeringAddress",
            )
            bgp_settings.peer_weight = AAZIntType(
                serialized_name="peerWeight",
            )

            ip_configurations = cls._schema_on_200.value.Element.properties.ip_configurations
            ip_configurations.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.ip_configurations.Element
            _element.etag = AAZStrType()
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.ip_configurations.Element.properties
            properties.private_ip_allocation_method = AAZStrType(
                serialized_name="privateIPAllocationMethod",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_ip_address = AAZObjectType(
                serialized_name="publicIPAddress",
            )
            _ListHelper._build_schema_sub_resource_read(properties.public_ip_address)
            properties.subnet = AAZObjectType()
            _ListHelper._build_schema_sub_resource_read(properties.subnet)

            sku = cls._schema_on_200.value.Element.properties.sku
            sku.capacity = AAZIntType()
            sku.name = AAZStrType()
            sku.tier = AAZStrType()

            vpn_client_configuration = cls._schema_on_200.value.Element.properties.vpn_client_configuration
            vpn_client_configuration.radius_server_address = AAZStrType(
                serialized_name="radiusServerAddress",
            )
            vpn_client_configuration.radius_server_secret = AAZStrType(
                serialized_name="radiusServerSecret",
            )
            vpn_client_configuration.vpn_client_address_pool = AAZObjectType(
                serialized_name="vpnClientAddressPool",
            )
            vpn_client_configuration.vpn_client_ipsec_policies = AAZListType(
                serialized_name="vpnClientIpsecPolicies",
            )
            vpn_client_configuration.vpn_client_protocols = AAZListType(
                serialized_name="vpnClientProtocols",
            )
            vpn_client_configuration.vpn_client_revoked_certificates = AAZListType(
                serialized_name="vpnClientRevokedCertificates",
            )
            vpn_client_configuration.vpn_client_root_certificates = AAZListType(
                serialized_name="vpnClientRootCertificates",
            )

            vpn_client_address_pool = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_address_pool
            vpn_client_address_pool.address_prefixes = AAZListType(
                serialized_name="addressPrefixes",
            )

            address_prefixes = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_address_pool.address_prefixes
            address_prefixes.Element = AAZStrType()

            vpn_client_ipsec_policies = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_ipsec_policies
            vpn_client_ipsec_policies.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_ipsec_policies.Element
            _element.dh_group = AAZStrType(
                serialized_name="dhGroup",
                flags={"required": True},
            )
            _element.ike_encryption = AAZStrType(
                serialized_name="ikeEncryption",
                flags={"required": True},
            )
            _element.ike_integrity = AAZStrType(
                serialized_name="ikeIntegrity",
                flags={"required": True},
            )
            _element.ipsec_encryption = AAZStrType(
                serialized_name="ipsecEncryption",
                flags={"required": True},
            )
            _element.ipsec_integrity = AAZStrType(
                serialized_name="ipsecIntegrity",
                flags={"required": True},
            )
            _element.pfs_group = AAZStrType(
                serialized_name="pfsGroup",
                flags={"required": True},
            )
            _element.sa_data_size_kilobytes = AAZIntType(
                serialized_name="saDataSizeKilobytes",
                flags={"required": True},
            )
            _element.sa_life_time_seconds = AAZIntType(
                serialized_name="saLifeTimeSeconds",
                flags={"required": True},
            )

            vpn_client_protocols = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_protocols
            vpn_client_protocols.Element = AAZStrType()

            vpn_client_revoked_certificates = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_revoked_certificates
            vpn_client_revoked_certificates.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_revoked_certificates.Element
            _element.etag = AAZStrType()
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_revoked_certificates.Element.properties
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.thumbprint = AAZStrType()

            vpn_client_root_certificates = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_root_certificates
            vpn_client_root_certificates.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_root_certificates.Element
            _element.etag = AAZStrType()
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_root_certificates.Element.properties
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_cert_data = AAZStrType(
                serialized_name="publicCertData",
                flags={"required": True},
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["List"]
