SCHEMA_CCAA = {}
SCHEMA_CCAA['id'] = int
SCHEMA_CCAA['ccaa'] = str

SCHEMA_PROVINCIA = {}
SCHEMA_PROVINCIA['id'] = int
SCHEMA_PROVINCIA['provincia'] = str
SCHEMA_PROVINCIA['idccaa'] = int

SCHEMA_POBLACION = {}
SCHEMA_POBLACION['id'] = int
SCHEMA_POBLACION['poblacion'] = str
SCHEMA_POBLACION['idprovincia'] = int

SCHEMA_HOUSING = {}
SCHEMA_HOUSING['longitude'] = float
SCHEMA_HOUSING['latitude'] = float
SCHEMA_HOUSING['housing_median_age'] = float
SCHEMA_HOUSING['total_rooms'] = float
SCHEMA_HOUSING['total_bedrooms'] = float
SCHEMA_HOUSING['population'] = float
SCHEMA_HOUSING['households'] = float
SCHEMA_HOUSING['median_income'] = float
SCHEMA_HOUSING['median_house_value'] = float
SCHEMA_HOUSING['ocean_proximity'] = str

SCHEMA_EMPRESA = {}
SCHEMA_EMPRESA['id'] = int
SCHEMA_EMPRESA['numero'] = str
SCHEMA_EMPRESA['empresa'] = str
SCHEMA_EMPRESA['direccion'] = str
SCHEMA_EMPRESA['cp'] = int
SCHEMA_EMPRESA['municipio'] = str
SCHEMA_EMPRESA['provincia'] = str
SCHEMA_EMPRESA['telefono'] = str
SCHEMA_EMPRESA['nif'] = str
SCHEMA_EMPRESA['alta'] = str
SCHEMA_EMPRESA['baja'] = str
SCHEMA_EMPRESA['web'] = str

SCHEMA_USUARIO = {}
SCHEMA_USUARIO['id'] = int
SCHEMA_USUARIO['nombre'] = str
SCHEMA_USUARIO['apellidos'] = str
SCHEMA_USUARIO['sexo'] = str
SCHEMA_USUARIO['nif'] = str
SCHEMA_USUARIO['ccaa'] = str
SCHEMA_USUARIO['provincia'] = str
SCHEMA_USUARIO['poblacion'] = str
SCHEMA_USUARIO['cp'] = int
SCHEMA_USUARIO['nacimiento'] = str  # 2024-05-27
SCHEMA_USUARIO['movil'] = str # 6.....
SCHEMA_USUARIO['fax'] = str   # 9......
SCHEMA_USUARIO['email'] = str

SCHEMA_URL = {}
SCHEMA_URL['date'] = str
SCHEMA_URL['url'] = str
SCHEMA_URL['visited'] = int
SCHEMA_URL['active'] = int
SCHEMA_URL['download'] = int
SCHEMA_URL['file'] = str
SCHEMA_URL['query'] = str

SCHEMA_FILE_SYSTEM = {}
SCHEMA_FILE_SYSTEM['path'] = str
SCHEMA_FILE_SYSTEM['name'] = str
SCHEMA_FILE_SYSTEM['file'] = str
SCHEMA_FILE_SYSTEM['size'] = int
SCHEMA_FILE_SYSTEM['access'] = str
SCHEMA_FILE_SYSTEM['last'] = str
SCHEMA_FILE_SYSTEM['create'] = str
