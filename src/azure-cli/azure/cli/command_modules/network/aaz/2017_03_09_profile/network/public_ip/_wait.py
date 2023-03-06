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
    "network public-ip wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/publicipaddresses/{}", "2015-06-15"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the public IP address.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.expand = AAZStrArg(
            options=["--expand"],
            help="Expands referenced resources.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PublicIPAddressesGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class PublicIPAddressesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{publicIpAddressName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "publicIpAddressName", self.ctx.args.name,
                    required=True,
                ),
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
                    "$expand", self.ctx.args.expand,
                ),
                **self.serialize_query_param(
                    "api-version", "2015-06-15",
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
            _WaitHelper._build_schema_public_ip_address_read(cls._schema_on_200)

            return cls._schema_on_200


class _WaitHelper:
    """Helper class for Wait"""

    _schema_ip_configuration_read = None

    @classmethod
    def _build_schema_ip_configuration_read(cls, _schema):
        if cls._schema_ip_configuration_read is not None:
            _schema.etag = cls._schema_ip_configuration_read.etag
            _schema.id = cls._schema_ip_configuration_read.id
            _schema.name = cls._schema_ip_configuration_read.name
            _schema.properties = cls._schema_ip_configuration_read.properties
            return

        cls._schema_ip_configuration_read = _schema_ip_configuration_read = AAZObjectType(
            flags={"read_only": True}
        )

        ip_configuration_read = _schema_ip_configuration_read
        ip_configuration_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        ip_configuration_read.id = AAZStrType(
            flags={"read_only": True},
        )
        ip_configuration_read.name = AAZStrType(
            flags={"read_only": True},
        )
        ip_configuration_read.properties = AAZObjectType(
            flags={"client_flatten": True, "read_only": True},
        )

        properties = _schema_ip_configuration_read.properties
        properties.private_ip_address = AAZStrType(
            serialized_name="privateIPAddress",
            flags={"read_only": True},
        )
        properties.private_ip_allocation_method = AAZStrType(
            serialized_name="privateIPAllocationMethod",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.public_ip_address = AAZObjectType(
            serialized_name="publicIPAddress",
        )
        cls._build_schema_public_ip_address_read(properties.public_ip_address)
        properties.subnet = AAZObjectType(
            flags={"read_only": True},
        )
        cls._build_schema_subnet_read(properties.subnet)

        _schema.etag = cls._schema_ip_configuration_read.etag
        _schema.id = cls._schema_ip_configuration_read.id
        _schema.name = cls._schema_ip_configuration_read.name
        _schema.properties = cls._schema_ip_configuration_read.properties

    _schema_network_interface_ip_configuration_read = None

    @classmethod
    def _build_schema_network_interface_ip_configuration_read(cls, _schema):
        if cls._schema_network_interface_ip_configuration_read is not None:
            _schema.etag = cls._schema_network_interface_ip_configuration_read.etag
            _schema.id = cls._schema_network_interface_ip_configuration_read.id
            _schema.name = cls._schema_network_interface_ip_configuration_read.name
            _schema.properties = cls._schema_network_interface_ip_configuration_read.properties
            return

        cls._schema_network_interface_ip_configuration_read = _schema_network_interface_ip_configuration_read = AAZObjectType(
            flags={"read_only": True}
        )

        network_interface_ip_configuration_read = _schema_network_interface_ip_configuration_read
        network_interface_ip_configuration_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        network_interface_ip_configuration_read.id = AAZStrType(
            flags={"read_only": True},
        )
        network_interface_ip_configuration_read.name = AAZStrType(
            flags={"read_only": True},
        )
        network_interface_ip_configuration_read.properties = AAZObjectType(
            flags={"client_flatten": True, "read_only": True},
        )

        properties = _schema_network_interface_ip_configuration_read.properties
        properties.load_balancer_backend_address_pools = AAZListType(
            serialized_name="loadBalancerBackendAddressPools",
            flags={"read_only": True},
        )
        properties.load_balancer_inbound_nat_rules = AAZListType(
            serialized_name="loadBalancerInboundNatRules",
            flags={"read_only": True},
        )
        properties.primary = AAZBoolType(
            flags={"read_only": True},
        )
        properties.private_ip_address = AAZStrType(
            serialized_name="privateIPAddress",
            flags={"read_only": True},
        )
        properties.private_ip_allocation_method = AAZStrType(
            serialized_name="privateIPAllocationMethod",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.public_ip_address = AAZObjectType(
            serialized_name="publicIPAddress",
        )
        cls._build_schema_public_ip_address_read(properties.public_ip_address)
        properties.subnet = AAZObjectType(
            flags={"read_only": True},
        )
        cls._build_schema_subnet_read(properties.subnet)

        load_balancer_backend_address_pools = _schema_network_interface_ip_configuration_read.properties.load_balancer_backend_address_pools
        load_balancer_backend_address_pools.Element = AAZObjectType(
            flags={"read_only": True},
        )

        _element = _schema_network_interface_ip_configuration_read.properties.load_balancer_backend_address_pools.Element
        _element.etag = AAZStrType(
            flags={"read_only": True},
        )
        _element.id = AAZStrType(
            flags={"read_only": True},
        )
        _element.name = AAZStrType(
            flags={"read_only": True},
        )
        _element.properties = AAZObjectType(
            flags={"client_flatten": True, "read_only": True},
        )

        properties = _schema_network_interface_ip_configuration_read.properties.load_balancer_backend_address_pools.Element.properties
        properties.backend_ip_configurations = AAZListType(
            serialized_name="backendIPConfigurations",
            flags={"read_only": True},
        )
        properties.load_balancing_rules = AAZListType(
            serialized_name="loadBalancingRules",
            flags={"read_only": True},
        )
        properties.outbound_nat_rule = AAZObjectType(
            serialized_name="outboundNatRule",
            flags={"read_only": True},
        )
        cls._build_schema_sub_resource_read(properties.outbound_nat_rule)
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        backend_ip_configurations = _schema_network_interface_ip_configuration_read.properties.load_balancer_backend_address_pools.Element.properties.backend_ip_configurations
        backend_ip_configurations.Element = AAZObjectType(
            flags={"read_only": True},
        )
        cls._build_schema_network_interface_ip_configuration_read(backend_ip_configurations.Element)

        load_balancing_rules = _schema_network_interface_ip_configuration_read.properties.load_balancer_backend_address_pools.Element.properties.load_balancing_rules
        load_balancing_rules.Element = AAZObjectType(
            flags={"read_only": True},
        )
        cls._build_schema_sub_resource_read(load_balancing_rules.Element)

        load_balancer_inbound_nat_rules = _schema_network_interface_ip_configuration_read.properties.load_balancer_inbound_nat_rules
        load_balancer_inbound_nat_rules.Element = AAZObjectType(
            flags={"read_only": True},
        )

        _element = _schema_network_interface_ip_configuration_read.properties.load_balancer_inbound_nat_rules.Element
        _element.etag = AAZStrType(
            flags={"read_only": True},
        )
        _element.id = AAZStrType(
            flags={"read_only": True},
        )
        _element.name = AAZStrType(
            flags={"read_only": True},
        )
        _element.properties = AAZObjectType(
            flags={"client_flatten": True, "read_only": True},
        )

        properties = _schema_network_interface_ip_configuration_read.properties.load_balancer_inbound_nat_rules.Element.properties
        properties.backend_ip_configuration = AAZObjectType(
            serialized_name="backendIPConfiguration",
            flags={"read_only": True},
        )
        cls._build_schema_network_interface_ip_configuration_read(properties.backend_ip_configuration)
        properties.backend_port = AAZIntType(
            serialized_name="backendPort",
            flags={"read_only": True},
        )
        properties.enable_floating_ip = AAZBoolType(
            serialized_name="enableFloatingIP",
            flags={"read_only": True},
        )
        properties.frontend_ip_configuration = AAZObjectType(
            serialized_name="frontendIPConfiguration",
            flags={"read_only": True},
        )
        cls._build_schema_sub_resource_read(properties.frontend_ip_configuration)
        properties.frontend_port = AAZIntType(
            serialized_name="frontendPort",
            flags={"read_only": True},
        )
        properties.idle_timeout_in_minutes = AAZIntType(
            serialized_name="idleTimeoutInMinutes",
            flags={"read_only": True},
        )
        properties.protocol = AAZStrType(
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        _schema.etag = cls._schema_network_interface_ip_configuration_read.etag
        _schema.id = cls._schema_network_interface_ip_configuration_read.id
        _schema.name = cls._schema_network_interface_ip_configuration_read.name
        _schema.properties = cls._schema_network_interface_ip_configuration_read.properties

    _schema_network_security_group_read = None

    @classmethod
    def _build_schema_network_security_group_read(cls, _schema):
        if cls._schema_network_security_group_read is not None:
            _schema.etag = cls._schema_network_security_group_read.etag
            _schema.id = cls._schema_network_security_group_read.id
            _schema.location = cls._schema_network_security_group_read.location
            _schema.name = cls._schema_network_security_group_read.name
            _schema.properties = cls._schema_network_security_group_read.properties
            _schema.tags = cls._schema_network_security_group_read.tags
            _schema.type = cls._schema_network_security_group_read.type
            return

        cls._schema_network_security_group_read = _schema_network_security_group_read = AAZObjectType(
            flags={"read_only": True}
        )

        network_security_group_read = _schema_network_security_group_read
        network_security_group_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        network_security_group_read.id = AAZStrType(
            flags={"read_only": True},
        )
        network_security_group_read.location = AAZStrType(
            flags={"read_only": True},
        )
        network_security_group_read.name = AAZStrType(
            flags={"read_only": True},
        )
        network_security_group_read.properties = AAZObjectType(
            flags={"client_flatten": True, "read_only": True},
        )
        network_security_group_read.tags = AAZDictType(
            flags={"read_only": True},
        )
        network_security_group_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_network_security_group_read.properties
        properties.default_security_rules = AAZListType(
            serialized_name="defaultSecurityRules",
            flags={"read_only": True},
        )
        properties.network_interfaces = AAZListType(
            serialized_name="networkInterfaces",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.resource_guid = AAZStrType(
            serialized_name="resourceGuid",
            flags={"read_only": True},
        )
        properties.security_rules = AAZListType(
            serialized_name="securityRules",
            flags={"read_only": True},
        )
        properties.subnets = AAZListType(
            flags={"read_only": True},
        )

        default_security_rules = _schema_network_security_group_read.properties.default_security_rules
        default_security_rules.Element = AAZObjectType(
            flags={"read_only": True},
        )
        cls._build_schema_security_rule_read(default_security_rules.Element)

        network_interfaces = _schema_network_security_group_read.properties.network_interfaces
        network_interfaces.Element = AAZObjectType(
            flags={"read_only": True},
        )

        _element = _schema_network_security_group_read.properties.network_interfaces.Element
        _element.etag = AAZStrType(
            flags={"read_only": True},
        )
        _element.id = AAZStrType(
            flags={"read_only": True},
        )
        _element.location = AAZStrType(
            flags={"read_only": True},
        )
        _element.name = AAZStrType(
            flags={"read_only": True},
        )
        _element.properties = AAZObjectType(
            flags={"client_flatten": True, "read_only": True},
        )
        _element.tags = AAZDictType(
            flags={"read_only": True},
        )
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_network_security_group_read.properties.network_interfaces.Element.properties
        properties.dns_settings = AAZObjectType(
            serialized_name="dnsSettings",
            flags={"read_only": True},
        )
        properties.enable_ip_forwarding = AAZBoolType(
            serialized_name="enableIPForwarding",
            flags={"read_only": True},
        )
        properties.ip_configurations = AAZListType(
            serialized_name="ipConfigurations",
            flags={"read_only": True},
        )
        properties.mac_address = AAZStrType(
            serialized_name="macAddress",
            flags={"read_only": True},
        )
        properties.network_security_group = AAZObjectType(
            serialized_name="networkSecurityGroup",
            flags={"read_only": True},
        )
        cls._build_schema_network_security_group_read(properties.network_security_group)
        properties.primary = AAZBoolType(
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.resource_guid = AAZStrType(
            serialized_name="resourceGuid",
            flags={"read_only": True},
        )
        properties.virtual_machine = AAZObjectType(
            serialized_name="virtualMachine",
            flags={"read_only": True},
        )
        cls._build_schema_sub_resource_read(properties.virtual_machine)

        dns_settings = _schema_network_security_group_read.properties.network_interfaces.Element.properties.dns_settings
        dns_settings.applied_dns_servers = AAZListType(
            serialized_name="appliedDnsServers",
            flags={"read_only": True},
        )
        dns_settings.dns_servers = AAZListType(
            serialized_name="dnsServers",
            flags={"read_only": True},
        )
        dns_settings.internal_dns_name_label = AAZStrType(
            serialized_name="internalDnsNameLabel",
            flags={"read_only": True},
        )
        dns_settings.internal_fqdn = AAZStrType(
            serialized_name="internalFqdn",
            flags={"read_only": True},
        )

        applied_dns_servers = _schema_network_security_group_read.properties.network_interfaces.Element.properties.dns_settings.applied_dns_servers
        applied_dns_servers.Element = AAZStrType(
            flags={"read_only": True},
        )

        dns_servers = _schema_network_security_group_read.properties.network_interfaces.Element.properties.dns_settings.dns_servers
        dns_servers.Element = AAZStrType(
            flags={"read_only": True},
        )

        ip_configurations = _schema_network_security_group_read.properties.network_interfaces.Element.properties.ip_configurations
        ip_configurations.Element = AAZObjectType(
            flags={"read_only": True},
        )
        cls._build_schema_network_interface_ip_configuration_read(ip_configurations.Element)

        tags = _schema_network_security_group_read.properties.network_interfaces.Element.tags
        tags.Element = AAZStrType(
            flags={"read_only": True},
        )

        security_rules = _schema_network_security_group_read.properties.security_rules
        security_rules.Element = AAZObjectType(
            flags={"read_only": True},
        )
        cls._build_schema_security_rule_read(security_rules.Element)

        subnets = _schema_network_security_group_read.properties.subnets
        subnets.Element = AAZObjectType(
            flags={"read_only": True},
        )
        cls._build_schema_subnet_read(subnets.Element)

        tags = _schema_network_security_group_read.tags
        tags.Element = AAZStrType(
            flags={"read_only": True},
        )

        _schema.etag = cls._schema_network_security_group_read.etag
        _schema.id = cls._schema_network_security_group_read.id
        _schema.location = cls._schema_network_security_group_read.location
        _schema.name = cls._schema_network_security_group_read.name
        _schema.properties = cls._schema_network_security_group_read.properties
        _schema.tags = cls._schema_network_security_group_read.tags
        _schema.type = cls._schema_network_security_group_read.type

    _schema_public_ip_address_read = None

    @classmethod
    def _build_schema_public_ip_address_read(cls, _schema):
        if cls._schema_public_ip_address_read is not None:
            _schema.etag = cls._schema_public_ip_address_read.etag
            _schema.id = cls._schema_public_ip_address_read.id
            _schema.location = cls._schema_public_ip_address_read.location
            _schema.name = cls._schema_public_ip_address_read.name
            _schema.properties = cls._schema_public_ip_address_read.properties
            _schema.tags = cls._schema_public_ip_address_read.tags
            _schema.type = cls._schema_public_ip_address_read.type
            return

        cls._schema_public_ip_address_read = _schema_public_ip_address_read = AAZObjectType()

        public_ip_address_read = _schema_public_ip_address_read
        public_ip_address_read.etag = AAZStrType()
        public_ip_address_read.id = AAZStrType()
        public_ip_address_read.location = AAZStrType()
        public_ip_address_read.name = AAZStrType(
            flags={"read_only": True},
        )
        public_ip_address_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        public_ip_address_read.tags = AAZDictType()
        public_ip_address_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_public_ip_address_read.properties
        properties.dns_settings = AAZObjectType(
            serialized_name="dnsSettings",
        )
        properties.idle_timeout_in_minutes = AAZIntType(
            serialized_name="idleTimeoutInMinutes",
        )
        properties.ip_address = AAZStrType(
            serialized_name="ipAddress",
        )
        properties.ip_configuration = AAZObjectType(
            serialized_name="ipConfiguration",
            flags={"read_only": True},
        )
        cls._build_schema_ip_configuration_read(properties.ip_configuration)
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.public_ip_allocation_method = AAZStrType(
            serialized_name="publicIPAllocationMethod",
        )
        properties.resource_guid = AAZStrType(
            serialized_name="resourceGuid",
        )

        dns_settings = _schema_public_ip_address_read.properties.dns_settings
        dns_settings.domain_name_label = AAZStrType(
            serialized_name="domainNameLabel",
        )
        dns_settings.fqdn = AAZStrType()
        dns_settings.reverse_fqdn = AAZStrType(
            serialized_name="reverseFqdn",
        )

        tags = _schema_public_ip_address_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_public_ip_address_read.etag
        _schema.id = cls._schema_public_ip_address_read.id
        _schema.location = cls._schema_public_ip_address_read.location
        _schema.name = cls._schema_public_ip_address_read.name
        _schema.properties = cls._schema_public_ip_address_read.properties
        _schema.tags = cls._schema_public_ip_address_read.tags
        _schema.type = cls._schema_public_ip_address_read.type

    _schema_security_rule_read = None

    @classmethod
    def _build_schema_security_rule_read(cls, _schema):
        if cls._schema_security_rule_read is not None:
            _schema.etag = cls._schema_security_rule_read.etag
            _schema.id = cls._schema_security_rule_read.id
            _schema.name = cls._schema_security_rule_read.name
            _schema.properties = cls._schema_security_rule_read.properties
            return

        cls._schema_security_rule_read = _schema_security_rule_read = AAZObjectType(
            flags={"read_only": True}
        )

        security_rule_read = _schema_security_rule_read
        security_rule_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        security_rule_read.id = AAZStrType(
            flags={"read_only": True},
        )
        security_rule_read.name = AAZStrType(
            flags={"read_only": True},
        )
        security_rule_read.properties = AAZObjectType(
            flags={"client_flatten": True, "read_only": True},
        )

        properties = _schema_security_rule_read.properties
        properties.access = AAZStrType(
            flags={"required": True, "read_only": True},
        )
        properties.description = AAZStrType(
            flags={"read_only": True},
        )
        properties.destination_address_prefix = AAZStrType(
            serialized_name="destinationAddressPrefix",
            flags={"required": True, "read_only": True},
        )
        properties.destination_port_range = AAZStrType(
            serialized_name="destinationPortRange",
            flags={"read_only": True},
        )
        properties.direction = AAZStrType(
            flags={"required": True, "read_only": True},
        )
        properties.priority = AAZIntType(
            flags={"read_only": True},
        )
        properties.protocol = AAZStrType(
            flags={"required": True, "read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.source_address_prefix = AAZStrType(
            serialized_name="sourceAddressPrefix",
            flags={"required": True, "read_only": True},
        )
        properties.source_port_range = AAZStrType(
            serialized_name="sourcePortRange",
            flags={"read_only": True},
        )

        _schema.etag = cls._schema_security_rule_read.etag
        _schema.id = cls._schema_security_rule_read.id
        _schema.name = cls._schema_security_rule_read.name
        _schema.properties = cls._schema_security_rule_read.properties

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType(
            flags={"read_only": True}
        )

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType(
            flags={"read_only": True},
        )

        _schema.id = cls._schema_sub_resource_read.id

    _schema_subnet_read = None

    @classmethod
    def _build_schema_subnet_read(cls, _schema):
        if cls._schema_subnet_read is not None:
            _schema.etag = cls._schema_subnet_read.etag
            _schema.id = cls._schema_subnet_read.id
            _schema.name = cls._schema_subnet_read.name
            _schema.properties = cls._schema_subnet_read.properties
            return

        cls._schema_subnet_read = _schema_subnet_read = AAZObjectType(
            flags={"read_only": True}
        )

        subnet_read = _schema_subnet_read
        subnet_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        subnet_read.id = AAZStrType(
            flags={"read_only": True},
        )
        subnet_read.name = AAZStrType(
            flags={"read_only": True},
        )
        subnet_read.properties = AAZObjectType(
            flags={"client_flatten": True, "read_only": True},
        )

        properties = _schema_subnet_read.properties
        properties.address_prefix = AAZStrType(
            serialized_name="addressPrefix",
            flags={"read_only": True},
        )
        properties.ip_configurations = AAZListType(
            serialized_name="ipConfigurations",
            flags={"read_only": True},
        )
        properties.network_security_group = AAZObjectType(
            serialized_name="networkSecurityGroup",
            flags={"read_only": True},
        )
        cls._build_schema_network_security_group_read(properties.network_security_group)
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.route_table = AAZObjectType(
            serialized_name="routeTable",
            flags={"read_only": True},
        )

        ip_configurations = _schema_subnet_read.properties.ip_configurations
        ip_configurations.Element = AAZObjectType(
            flags={"read_only": True},
        )
        cls._build_schema_ip_configuration_read(ip_configurations.Element)

        route_table = _schema_subnet_read.properties.route_table
        route_table.etag = AAZStrType(
            flags={"read_only": True},
        )
        route_table.id = AAZStrType(
            flags={"read_only": True},
        )
        route_table.location = AAZStrType(
            flags={"read_only": True},
        )
        route_table.name = AAZStrType(
            flags={"read_only": True},
        )
        route_table.properties = AAZObjectType(
            flags={"client_flatten": True, "read_only": True},
        )
        route_table.tags = AAZDictType(
            flags={"read_only": True},
        )
        route_table.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_subnet_read.properties.route_table.properties
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.routes = AAZListType(
            flags={"read_only": True},
        )
        properties.subnets = AAZListType(
            flags={"read_only": True},
        )

        routes = _schema_subnet_read.properties.route_table.properties.routes
        routes.Element = AAZObjectType(
            flags={"read_only": True},
        )

        _element = _schema_subnet_read.properties.route_table.properties.routes.Element
        _element.etag = AAZStrType(
            flags={"read_only": True},
        )
        _element.id = AAZStrType(
            flags={"read_only": True},
        )
        _element.name = AAZStrType(
            flags={"read_only": True},
        )
        _element.properties = AAZObjectType(
            flags={"client_flatten": True, "read_only": True},
        )

        properties = _schema_subnet_read.properties.route_table.properties.routes.Element.properties
        properties.address_prefix = AAZStrType(
            serialized_name="addressPrefix",
            flags={"read_only": True},
        )
        properties.next_hop_ip_address = AAZStrType(
            serialized_name="nextHopIpAddress",
            flags={"read_only": True},
        )
        properties.next_hop_type = AAZStrType(
            serialized_name="nextHopType",
            flags={"required": True, "read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        subnets = _schema_subnet_read.properties.route_table.properties.subnets
        subnets.Element = AAZObjectType(
            flags={"read_only": True},
        )
        cls._build_schema_subnet_read(subnets.Element)

        tags = _schema_subnet_read.properties.route_table.tags
        tags.Element = AAZStrType(
            flags={"read_only": True},
        )

        _schema.etag = cls._schema_subnet_read.etag
        _schema.id = cls._schema_subnet_read.id
        _schema.name = cls._schema_subnet_read.name
        _schema.properties = cls._schema_subnet_read.properties


__all__ = ["Wait"]
