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
    "network traffic-manager endpoint update",
)
class Update(AAZCommand):
    """Update a traffic manager endpoint.

    :example: Update a traffic manager endpoint to change its weight.
        az network traffic-manager endpoint update -g MyResourceGroup --profile-name MyTmProfile -n MyEndpoint --weight 20 --type azureEndpoints

    :example: Update a traffic manager endpoint. (autogenerated)
        az network traffic-manager endpoint update --name MyEndpoint --profile-name MyTmProfile --resource-group MyResourceGroup --target webserver.mysite.com --type azureEndpoints

    :example: Update a traffic manager endpoint. (autogenerated)
        az network traffic-manager endpoint update --endpoint-status Enabled --name MyEndpoint --profile-name MyTmProfile --resource-group MyResourceGroup --type azureEndpoints

    :example: Update a traffic manager endpoint.
        az network traffic-manager endpoint update -n MyTmEndpoint --type azureEndpoints --profile-name MyTmProfile -g MyResourceGroup --subnets [{first:10.0.0.0,scope:24}]
        az network traffic-manager endpoint update -n MyTmEndpoint --type azureEndpoints --profile-name MyTmProfile -g MyResourceGroup --subnets [{first:10.0.0.0,last:11.0.0.0}]
    """

    _aaz_info = {
        "version": "2022-04-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/trafficmanagerprofiles/{}/{}/{}", "2022-04-01-preview"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

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
            help="Endpoint name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.type = AAZStrArg(
            options=["-t", "--type"],
            help="Endpoint type.  Allowed values: azureEndpoints, externalEndpoints, nestedEndpoints.",
            required=True,
            id_part="child_type_1",
            enum={"AzureEndpoints": "AzureEndpoints", "ExternalEndpoints": "ExternalEndpoints", "NestedEndpoints": "NestedEndpoints"},
        )
        _args_schema.profile_name = AAZStrArg(
            options=["--profile-name"],
            help="Name of parent profile.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.always_serve = AAZStrArg(
            options=["--always-serve"],
            help="If Always Serve is enabled, probing for endpoint health will be disabled and endpoints will be included in the traffic routing method.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )

        # define Arg Group "Parameters"

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.custom_headers = AAZListArg(
            options=["--custom-headers"],
            arg_group="Properties",
            help="Space-separated list of custom headers in KEY=VALUE format.",
            nullable=True,
        )
        _args_schema.endpoint_location = AAZStrArg(
            options=["--endpoint-location"],
            arg_group="Properties",
            help="Location of the external or nested endpoints when using the 'Performance' routing method.",
            nullable=True,
        )
        _args_schema.endpoint_monitor_status = AAZStrArg(
            options=["--endpoint-monitor-status"],
            arg_group="Properties",
            help="The monitoring status of the endpoint.",
            nullable=True,
            enum={"CheckingEndpoint": "CheckingEndpoint", "Degraded": "Degraded", "Disabled": "Disabled", "Inactive": "Inactive", "Online": "Online", "Stopped": "Stopped"},
        )
        _args_schema.endpoint_status = AAZStrArg(
            options=["--endpoint-status"],
            arg_group="Properties",
            help="The status of the endpoint. If enabled the endpoint is probed for endpoint health and included in the traffic routing method.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        _args_schema.geo_mapping = AAZListArg(
            options=["--geo-mapping"],
            arg_group="Properties",
            help="Space-separated list of country/region codes mapped to this endpoint when using the 'Geographic' routing method.",
            nullable=True,
        )
        _args_schema.min_child_endpoints = AAZIntArg(
            options=["--min-child-endpoints"],
            arg_group="Properties",
            help="The minimum number of endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.",
            nullable=True,
        )
        _args_schema.min_child_ipv4 = AAZIntArg(
            options=["--min-child-ipv4"],
            arg_group="Properties",
            help="The minimum number of IPv4 (DNS record type A) endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.",
            nullable=True,
        )
        _args_schema.min_child_ipv6 = AAZIntArg(
            options=["--min-child-ipv6"],
            arg_group="Properties",
            help="The minimum number of IPv6 (DNS record type AAAA) endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.",
            nullable=True,
        )
        _args_schema.priority = AAZIntArg(
            options=["--priority"],
            arg_group="Properties",
            help="Priority of the endpoint when using the 'Priority' traffic routing method. Values range from 1 to 1000, with lower values representing higher priority.",
            nullable=True,
        )
        _args_schema.subnets = AAZListArg(
            options=["--subnets"],
            arg_group="Properties",
            help="Space-separated list of subnet CIDR prefixes or subnet ranges.",
            nullable=True,
        )
        _args_schema.target = AAZStrArg(
            options=["--target"],
            arg_group="Properties",
            help="Fully-qualified DNS name of the endpoint.",
            nullable=True,
        )
        _args_schema.target_resource_id = AAZStrArg(
            options=["--target-resource-id"],
            arg_group="Properties",
            help="The Azure Resource URI of the of the endpoint. Not applicable to endpoints of type 'ExternalEndpoints'.",
            nullable=True,
        )
        _args_schema.weight = AAZIntArg(
            options=["--weight"],
            arg_group="Properties",
            help="Weight of the endpoint when using the 'Weighted' traffic routing method. Values range from 1 to 1000.",
            nullable=True,
        )

        custom_headers = cls._args_schema.custom_headers
        custom_headers.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.custom_headers.Element
        _element.name = AAZStrArg(
            options=["name"],
            help="Header name.",
            nullable=True,
        )
        _element.value = AAZStrArg(
            options=["value"],
            help="Header value.",
            nullable=True,
        )

        geo_mapping = cls._args_schema.geo_mapping
        geo_mapping.Element = AAZStrArg(
            nullable=True,
        )

        subnets = cls._args_schema.subnets
        subnets.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.subnets.Element
        _element.first = AAZStrArg(
            options=["first"],
            help="First address in the subnet.",
            nullable=True,
        )
        _element.last = AAZStrArg(
            options=["last"],
            help="Last address in the subnet.",
            nullable=True,
        )
        _element.scope = AAZIntArg(
            options=["scope"],
            help="Block size (number of leading bits in the subnet mask).",
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.EndpointsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.EndpointsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class EndpointsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}/{endpointType}/{endpointName}",
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
                    "endpointName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "endpointType", self.ctx.args.type,
                    required=True,
                ),
                **self.serialize_url_param(
                    "profileName", self.ctx.args.profile_name,
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
                    "api-version", "2022-04-01-preview",
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
            _UpdateHelper._build_schema_endpoint_read(cls._schema_on_200)

            return cls._schema_on_200

    class EndpointsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}/{endpointType}/{endpointName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "endpointName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "endpointType", self.ctx.args.type,
                    required=True,
                ),
                **self.serialize_url_param(
                    "profileName", self.ctx.args.profile_name,
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
                    "api-version", "2022-04-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_endpoint_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("name", AAZStrType, ".name")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("alwaysServe", AAZStrType, ".always_serve")
                properties.set_prop("customHeaders", AAZListType, ".custom_headers")
                properties.set_prop("endpointLocation", AAZStrType, ".endpoint_location")
                properties.set_prop("endpointMonitorStatus", AAZStrType, ".endpoint_monitor_status")
                properties.set_prop("endpointStatus", AAZStrType, ".endpoint_status")
                properties.set_prop("geoMapping", AAZListType, ".geo_mapping")
                properties.set_prop("minChildEndpoints", AAZIntType, ".min_child_endpoints")
                properties.set_prop("minChildEndpointsIPv4", AAZIntType, ".min_child_ipv4")
                properties.set_prop("minChildEndpointsIPv6", AAZIntType, ".min_child_ipv6")
                properties.set_prop("priority", AAZIntType, ".priority")
                properties.set_prop("subnets", AAZListType, ".subnets")
                properties.set_prop("target", AAZStrType, ".target")
                properties.set_prop("targetResourceId", AAZStrType, ".target_resource_id")
                properties.set_prop("weight", AAZIntType, ".weight")

            custom_headers = _builder.get(".properties.customHeaders")
            if custom_headers is not None:
                custom_headers.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.customHeaders[]")
            if _elements is not None:
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("value", AAZStrType, ".value")

            geo_mapping = _builder.get(".properties.geoMapping")
            if geo_mapping is not None:
                geo_mapping.set_elements(AAZStrType, ".")

            subnets = _builder.get(".properties.subnets")
            if subnets is not None:
                subnets.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.subnets[]")
            if _elements is not None:
                _elements.set_prop("first", AAZStrType, ".first")
                _elements.set_prop("last", AAZStrType, ".last")
                _elements.set_prop("scope", AAZIntType, ".scope")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_endpoint_read = None

    @classmethod
    def _build_schema_endpoint_read(cls, _schema):
        if cls._schema_endpoint_read is not None:
            _schema.id = cls._schema_endpoint_read.id
            _schema.name = cls._schema_endpoint_read.name
            _schema.properties = cls._schema_endpoint_read.properties
            _schema.type = cls._schema_endpoint_read.type
            return

        cls._schema_endpoint_read = _schema_endpoint_read = AAZObjectType()

        endpoint_read = _schema_endpoint_read
        endpoint_read.id = AAZStrType()
        endpoint_read.name = AAZStrType()
        endpoint_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        endpoint_read.type = AAZStrType()

        properties = _schema_endpoint_read.properties
        properties.always_serve = AAZStrType(
            serialized_name="alwaysServe",
        )
        properties.custom_headers = AAZListType(
            serialized_name="customHeaders",
        )
        properties.endpoint_location = AAZStrType(
            serialized_name="endpointLocation",
        )
        properties.endpoint_monitor_status = AAZStrType(
            serialized_name="endpointMonitorStatus",
        )
        properties.endpoint_status = AAZStrType(
            serialized_name="endpointStatus",
        )
        properties.geo_mapping = AAZListType(
            serialized_name="geoMapping",
        )
        properties.min_child_endpoints = AAZIntType(
            serialized_name="minChildEndpoints",
        )
        properties.min_child_endpoints_i_pv4 = AAZIntType(
            serialized_name="minChildEndpointsIPv4",
        )
        properties.min_child_endpoints_i_pv6 = AAZIntType(
            serialized_name="minChildEndpointsIPv6",
        )
        properties.priority = AAZIntType()
        properties.subnets = AAZListType()
        properties.target = AAZStrType()
        properties.target_resource_id = AAZStrType(
            serialized_name="targetResourceId",
        )
        properties.weight = AAZIntType()

        custom_headers = _schema_endpoint_read.properties.custom_headers
        custom_headers.Element = AAZObjectType()

        _element = _schema_endpoint_read.properties.custom_headers.Element
        _element.name = AAZStrType()
        _element.value = AAZStrType()

        geo_mapping = _schema_endpoint_read.properties.geo_mapping
        geo_mapping.Element = AAZStrType()

        subnets = _schema_endpoint_read.properties.subnets
        subnets.Element = AAZObjectType()

        _element = _schema_endpoint_read.properties.subnets.Element
        _element.first = AAZStrType()
        _element.last = AAZStrType()
        _element.scope = AAZIntType()

        _schema.id = cls._schema_endpoint_read.id
        _schema.name = cls._schema_endpoint_read.name
        _schema.properties = cls._schema_endpoint_read.properties
        _schema.type = cls._schema_endpoint_read.type


__all__ = ["Update"]
