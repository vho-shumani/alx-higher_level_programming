#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: python object pointer.
 */
void print_python_list_info(PyObject *p)
{
	int i, size_list;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", elem, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
	}
