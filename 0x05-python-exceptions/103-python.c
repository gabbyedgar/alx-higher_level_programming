#include "Python.h"

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_float - print a PyFloatObject as a double
 * @p: pointer to PyObject, which also be a PyFloatObject
 */
void print_python_float(PyObject *p)
{
	char *f_as_s;

	printf("[.] float object info\n");
	if (p != NULL && PyFloat_Check(p))
	{
		f_as_s = PyOS_double_to_string(PyFloat_AsDouble(p),
					       'r',
					       0,
					       Py_DTSF_ADD_DOT_0,
					       NULL);
		if (f_as_s == NULL)
			printf("  value: %f\n", PyFloat_AsDouble(p));
		else
		{
			printf("  value: %s\n", f_as_s);
			PyMem_Free(f_as_s);
		}
	}
	else
		printf("  [ERROR] Invalid Float Object\n");
	fflush(stdout);
}

/**
 * print_python_bytes - print information about Python bytes object
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t bytes_size, i;
	char *bytes_string;

	printf("[.] bytes object info\n");
	if (p != NULL && PyBytes_Check(p))
	{
		bytes_string = ((PyBytesObject *)p)->ob_sval;
		bytes_size = ((PyVarObject *)p)->ob_size;
		printf("  size: %ld\n", bytes_size);
		printf("  trying string: %s\n", bytes_string);
		printf("  first %ld bytes:",
		       bytes_size + 1 < 10 ? bytes_size + 1 : 10);
		for (i = 0; i < bytes_size + 1 && i < 10; i++)
			printf(" %02x", bytes_string[i] & 0xff);
		putchar('\n');
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
	fflush(stdout);
}

/**
 * print_python_list - print information about Python list object
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	PyObject *item;
	PyListObject *list;
	Py_ssize_t list_size, list_alloc, i;
	const char *type;

	printf("[*] Python list info\n");
	if (p != NULL && PyList_Check(p))
	{
		list_size = ((PyVarObject *)p)->ob_size;
		if (list_size < 0)
			return;
		list = (PyListObject *)p;
		list_alloc = list->allocated;
		if (list_alloc < 0)
			return;
		printf("[*] Size of the Python List = %ld\n", list_size);
		printf("[*] Allocated = %ld\n", list_alloc);
		for (i = 0; i < list_size; i++)
		{
			item = list->ob_item[i];
			type = item->ob_type->tp_name;
			printf("Element %ld: %s\n", i, type);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
	fflush(stdout);
}
