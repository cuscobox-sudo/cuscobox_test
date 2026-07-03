#!/usr/bin/env python3
"""
간단한 콘솔 기반 Todo 리스트 프로그램
"""

import json
import os
from datetime import datetime

TODO_FILE = "todos.json"


def load_todos():
    """파일에서 Todo 리스트를 로드합니다."""
    if os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []


def save_todos(todos):
    """Todo 리스트를 파일에 저장합니다."""
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2, ensure_ascii=False)


def add_todo(todos):
    """새로운 Todo를 추가합니다."""
    title = input("Todo 제목: ").strip()
    if not title:
        print("제목은 비어 있을 수 없습니다.")
        return

    description = input("설명 (선택사항): ").strip()
    due_date = input("마감일 (YYYY-MM-DD, 선택사항): ").strip()
    priority = input("우선순위 (High/Medium/Low, 선택사항): ").strip()

    todo = {
        "id": len(todos) + 1,
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    todos.append(todo)
    save_todos(todos)
    print(f"Todo '{title}'이(가) 추가되었습니다!")


def list_todos(todos):
    """모든 Todo를 목록으로 표시합니다."""
    if not todos:
        print("Todo가 없습니다.")
        return

    print("\n=== Todo 리스트 ===")
    for todo in todos:
        status = "✓" if todo["completed"] else "○"
        priority = todo.get("priority", "None")
        due_date = todo.get("due_date", "None")
        print(f"{status} ID: {todo['id']} | 우선순위: {priority} | 마감일: {due_date}")
        print(f"  제목: {todo['title']}")
        if todo["description"]:
            print(f"  설명: {todo['description']}")
        print(f"  생성일: {todo['created_at']}")
        print("-" * 40)


def complete_todo(todos):
    """Todo를 완료 상태로 표시합니다."""
    list_todos(todos)
    try:
        todo_id = int(input("완료할 Todo ID: "))
        for todo in todos:
            if todo["id"] == todo_id:
                todo["completed"] = True
                save_todos(todos)
                print(f"Todo '{todo['title']}'이(가) 완료되었습니다!")
                return
        print("해당 ID의 Todo를 찾을 수 없습니다.")
    except ValueError:
        print("유효한 ID를 입력해주세요.")


def delete_todo(todos):
    """Todo를 삭제합니다."""
    list_todos(todos)
    try:
        todo_id = int(input("삭제할 Todo ID: "))
        for i, todo in enumerate(todos):
            if todo["id"] == todo_id:
                del todos[i]
                save_todos(todos)
                print(f"Todo '{todo['title']}'이(가) 삭제되었습니다!")
                return
        print("해당 ID의 Todo를 찾을 수 없습니다.")
    except ValueError:
        print("유효한 ID를 입력해주세요.")


def filter_todos(todos):
    """Todo를 필터링하여 표시합니다."""
    print("\n=== Todo 필터링 ===")
    print("1. 완료된 Todo만 보기")
    print("2. 미완료된 Todo만 보기")
    print("3. 우선순위별 보기")
    print("4. 마감일별 보기")
    choice = input("선택: ").strip()

    if choice == "1":
        filtered = [todo for todo in todos if todo["completed"]]
    elif choice == "2":
        filtered = [todo for todo in todos if not todo["completed"]]
    elif choice == "3":
        priority = input("우선순위 (High/Medium/Low): ").strip()
        filtered = [todo for todo in todos if todo.get("priority", "").lower() == priority.lower()]
    elif choice == "4":
        due_date = input("마감일 (YYYY-MM-DD): ").strip()
        filtered = [todo for todo in todos if todo.get("due_date", "") == due_date]
    else:
        print("잘못된 선택입니다.")
        return

    if not filtered:
        print("해당 조건에 맞는 Todo가 없습니다.")
    else:
        list_todos(filtered)


def main():
    """메인 메뉴를 표시하고 사용자 입력을 처리합니다."""
    todos = load_todos()

    while True:
        print("\n=== Todo 리스트 프로그램 ===")
        print("1. Todo 추가")
        print("2. Todo 목록 보기")
        print("3. Todo 완료")
        print("4. Todo 삭제")
        print("5. Todo 필터링")
        print("6. 종료")

        choice = input("선택: ").strip()

        if choice == "1":
            add_todo(todos)
        elif choice == "2":
            list_todos(todos)
        elif choice == "3":
            complete_todo(todos)
        elif choice == "4":
            delete_todo(todos)
        elif choice == "5":
            filter_todos(todos)
        elif choice == "6":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()
