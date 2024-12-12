import sqlite3
from typing import List, Dict, Any


class SQLiteTool:
    def __init__(self, db_path: str):
        """
        初始化 SQLite 工具类
        :param db_path: SQLite 数据库文件的路径
        """
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """
        连接到 SQLite 数据库
        """
        try:
            self.connection = sqlite3.connect(self.db_path)
            print(f"成功连接到数据库: {self.db_path}")
        except sqlite3.Error as e:
            print(f"连接数据库时出错: {e}")
            raise

    def close(self):
        """
        关闭数据库连接
        """
        if self.connection:
            self.connection.close()
            print("数据库连接已关闭")

    def execute_query(self, query: str, params: tuple = None) -> List[Dict[str, Any]]:
        """
        执行 SQL 查询并返回结果
        :param query: SQL 查询语句
        :param params: 查询参数（可选）
        :return: 查询结果列表，每个结果是一个字典
        """
        if not self.connection:
            self.connect()

        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            # 获取列名
            column_names = [description[0] for description in cursor.description]

            # 获取查询结果
            rows = cursor.fetchall()
            result = [dict(zip(column_names, row)) for row in rows]
            return result
        except sqlite3.Error as e:
            print(f"执行查询时出错: {e}")
            raise
        finally:
            cursor.close()

    def execute_non_query(self, query: str, params: tuple = None):
        """
        执行非查询 SQL 语句（如插入、更新、删除）
        :param query: SQL 语句
        :param params: 参数（可选）
        """
        if not self.connection:
            self.connect()

        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("SQL 语句执行成功")
        except sqlite3.Error as e:
            print(f"执行 SQL 语句时出错: {e}")
            self.connection.rollback()
            raise
        finally:
            cursor.close()

    def create_table(self, table_name: str, columns: Dict[str, str]):
        """
        创建表
        :param table_name: 表名
        :param columns: 列定义字典，键为列名，值为列类型和约束
        """
        column_definitions = ", ".join(f"{name} {definition}" for name, definition in columns.items())
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
        self.execute_non_query(query)
        print(f"表 {table_name} 创建成功")

    def insert_data(self, table_name: str, data: Dict[str, Any]):
        """
        插入数据到表中
        :param table_name: 表名
        :param data: 数据字典，键为列名，值为数据
        """
        columns = ", ".join(data.keys())
        placeholders = ", ".join("?" for _ in data.values())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.execute_non_query(query, tuple(data.values()))
        print(f"数据插入成功: {data}")

    def update_data(self, table_name: str, data: Dict[str, Any], condition: str):
        """
        更新表中的数据
        :param table_name: 表名
        :param data: 数据字典，键为列名，值为新数据
        :param condition: 更新条件（SQL WHERE 子句）
        """
        set_clause = ", ".join(f"{key} = ?" for key in data.keys())
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        self.execute_non_query(query, tuple(data.values()))
        print(f"数据更新成功: {data}")

    def delete_data(self, table_name: str, condition: str):
        """
        删除表中的数据
        :param table_name: 表名
        :param condition: 删除条件（SQL WHERE 子句）
        """
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.execute_non_query(query)
        print(f"数据删除成功: 条件为 {condition}")

    def query_data(self, table_name: str, condition: str = None) -> List[Dict[str, Any]]:
        """
        查询表中的数据
        :param table_name: 表名
        :param condition: 查询条件（SQL WHERE 子句，可选）
        :return: 查询结果列表，每个结果是一个字典
        """
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        return self.execute_query(query)