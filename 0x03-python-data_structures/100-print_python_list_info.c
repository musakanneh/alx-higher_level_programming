#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * print_python_list_info- Prints some basic info about Python lists.
 * @p: PyObject
 */

void print_python_list_info(__attribute__((unused)) PyObject *p)
{
	int i;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < Py_SIZE(p); i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
