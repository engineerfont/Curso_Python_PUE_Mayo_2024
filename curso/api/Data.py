import datetime
import curso.api.Ficheros as File
import curso.api.Input as Util

def data_record(filename, header=False, schema=None, separator=None):
    separator = separator if separator else ';'
    data_file = File.list_file_text(filename)
    fields = data_file[0].strip().split(separator)
    names_header = fields
    if not header:
        if schema:
            names_header = list(schema.keys())
        else:
            names_header = list(map(lambda s: f'_c{s}', range(len(fields))))

    def convert_field(n, field):
        return schema[names_header[n]](field)

    def record(line):
        values = line.strip().split(separator)
        if schema:
            return {names_header[i]: convert_field(i, values[i]) for i in range(len(values))}
        else:
            return {names_header[i]: values[i] for i in range(len(values))}

    return list(map(record, data_file[1 if header else 0:]))
