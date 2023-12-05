#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: python object pointer.
 */
void print_python_list_info(PyObject *p)
{
	Py-ssize_t size_list, i;

	size_list = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size_list; i++)
	{
		printf("Element %zd: %s\n", elem, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
