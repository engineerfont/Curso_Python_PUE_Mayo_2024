import datetime
import curso.api.Ficheros as File
import curso.api.Input as Util

def data_record(filename, header=False, schema=None, separator=None):
    separator = separator if separator else ';'
    names_header = ''

    def tipo(type):
        if type == int:
            return Util.to_int
        elif type == float:
            return Util.to_float
        elif type == complex:
            return Util.to_complex
        elif type == bool:
            return Util.to_bool
        elif type == datetime.date:
            return Util.to_date
        else:
            return Util.to_str

    def convert_field(n, field):
        return tipo(schema[names_header[n]])(field)

    def record(line):
        values = line.strip().split(separator)
        if schema:
            return {names_header[i]: convert_field(i, values[i]) for i in range(len(values))}
        else:
            return {names_header[i]: values[i] for i in range(len(values))}

    data_file = File.list_file_text(filename)
    fields = data_file[0].strip().split(separator)
    if header:
        names_header = fields
    else:
        if schema:
            names_header = schema.keys()
        else:
            # names_header = [f'_c{i}' for i in range(len(fields))]
            names_header = list(map(lambda s: f'_c{s}', range(len(fields))))
    #return [record(data) for data in data_file[1 if header else 0:]]
    return list(map(record, data_file[1 if header else 0:]))
