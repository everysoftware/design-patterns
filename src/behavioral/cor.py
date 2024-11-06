"""
Chain of Responsibility is a behavioral design pattern that allows requests to be passed along a chain
of handlers. Each handler decides whether it can handle the request, and if it cannot, passes it on to the next
handler in the chain.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class LeaveRequest:
    def __init__(self, days: int) -> None:
        self.days = days


class LeaveResponse:
    def __init__(self, reviewer_position: str, approved: bool) -> None:
        self.reviewer_position = reviewer_position
        self.approved = approved


class Reviewer(ABC):
    def __init__(self, next_reviewer: Reviewer | None = None) -> None:
        self.next = next_reviewer

    @abstractmethod
    def approve(self, request: LeaveRequest) -> LeaveResponse: ...


class TeamLead(Reviewer):
    def approve(self, request: LeaveRequest) -> LeaveResponse:
        if request.days <= 1:
            return LeaveResponse("TeamLead", True)
        if self.next is None:
            return LeaveResponse("TeamLead", False)
        return self.next.approve(request)


class Manager(Reviewer):
    def approve(self, request: LeaveRequest) -> LeaveResponse:
        if request.days <= 14:
            return LeaveResponse("Manager", True)
        if self.next is None:
            return LeaveResponse("Manager", False)
        return self.next.approve(request)


class Director(Reviewer):
    def approve(self, request: LeaveRequest) -> LeaveResponse:
        if request.days > 14:
            return LeaveResponse("Director", True)
        if self.next is None:
            return LeaveResponse("Director", False)
        return self.next.approve(request)
