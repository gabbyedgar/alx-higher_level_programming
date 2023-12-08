#include "Python.h"

/**
 * print_python_list_info - print info about a python list object
 * @p: pointer to PyObject, which should be castable to a PyListObject
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;
	const char *type;
	Py_ssize_t l_size, l_allocated;
	PyObject *element;
	PyListObject *newp;

	if (PyList_Check(p))
	{
		newp = (PyListObject *) p;
		l_size = PyList_Size(p);
		if (l_size < 0)
			return;
		l_allocated = newp->allocated;
		if (l_allocated < 0)
			return;
		printf("[*] Size of the Python List = %ld\n", l_size);
		printf("[*] Allocated = %ld\n", l_allocated);

		for (i = 0; i < l_size; i++)
		{
			element = newp->ob_item[i];
			type = Py_TYPE(element)->tp_name;
			printf("Element %ld: %s\n", i, type);
		}
	}
}
