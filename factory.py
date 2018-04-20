"""
Handles the instantiation of SAP SuccessFactors' employees.
"""

import random

from developer import Developer
from projectmanager import ProjectManager
from sales import Sales
from support import Support


class EmployeeFactory:
    """
    Handles the instantiation of SAP SuccessFactors' employees
    """

    @staticmethod
    def random_employee(employee_type):
        """
        Returns an employee of the corresponding type with random attributes.
        """
        if employee_type == 'developer':
            return Developer(**Developer.random_attrs())
        if employee_type == 'sales':
            return Sales(**Sales.random_attrs())
        if employee_type == 'project_manager':
            return ProjectManager(**ProjectManager.random_attrs())
        if employee_type == 'support':
            return Support(**Support.random_attrs())
        err_msg = (
            '{} employee type is not supported.\n'.format(type),
            'Allowed values are: \'developer\', \'project_manager\', \'sales\' or \'support\'',
        )
        raise ValueError(err_msg)

    @staticmethod
    def generate_workforce(n_employees, ratios):
        """
        Generates a workforce of n_employees based on ratios.
        """
        workforce = []
        for employee_type, ratio in ratios.items():
            n_employees_current_type = int(ratio * n_employees)
            for _ in range(n_employees_current_type):
                workforce.append(EmployeeFactory.random_employee(employee_type))
        random.shuffle(workforce)
        return workforce
