# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

''' Pg data types. We need to make sure all the data types are defined with name starting with DATATYPE_ as we
pull them into the array of system datatypes '''

''' Standard Data Types '''

DATATYPE_NULL = 'NULL'
DATATYPE_CHAR = 'char'
DATATYPE_BIGINT = 'int8'
DATATYPE_SMALLINT = 'int2'
DATATYPE_INTEGER = 'int4'
DATATYPE_BOOL = 'bool'
DATATYPE_REAL = 'float4'
DATATYPE_DOUBLE = 'float8'
DATATYPE_NUMERIC = 'numeric'
DATATYPE_VARCHAR = 'varchar'
DATATYPE_TEXT = 'text'
DATATYPE_DATE = 'date'
DATATYPE_TIME = 'time'
DATATYPE_TIME_WITH_TIMEZONE = 'timetz'
DATATYPE_TIMESTAMP = 'timestamp'
DATATYPE_TIMESTAMP_WITH_TIMEZONE = 'timestamptz'
DATATYPE_INTERVAL = 'interval'
DATATYPE_UUID = 'uuid'

''' Non-standard Data Types '''

DATATYPE_SMALLSERIAL = 'smallserial'
DATATYPE_SERIAL = 'serial'
DATATYPE_BIGSERIAL = 'bigserial'
DATATYPE_MONEY = 'money'
DATATYPE_BYTEA = 'bytea'
DATATYPE_ENUM = 'enum'
DATATYPE_POINT = 'point'
DATATYPE_LINE = 'line'
DATATYPE_LSEG = 'lseg'
DATATYPE_BOX = 'box'
DATATYPE_PATH = 'path'
DATATYPE_POLYGON = 'polygon'
DATATYPE_CIRCLE = 'circle'
DATATYPE_CIDR = 'cidr'
DATATYPE_INET = 'inet'
DATATYPE_MACADDR = 'macaddr'
DATATYPE_BIT = 'bit'
DATATYPE_BIT_VARYING = 'bit_varying'
DATATYPE_XML = 'xml'
DATATYPE_JSON = 'json'
DATATYPE_ARRAY = 'array'
DATATYPE_INT4RANGE = 'int4range'
DATATYPE_INT8RANGE = 'int8range'
DATATYPE_NUMRANGE = 'numrange'
DATATYPE_TSRANGE = 'tsrange'
DATATYPE_TSTZRANGE = 'tstzrange'
DATATYPE_DATERANGE = 'daterange'