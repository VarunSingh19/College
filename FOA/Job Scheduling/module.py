print("Priyanka Tiwari:1000")

class job:
    def __init__(self, task_id, deadline, profit):
        self.task_id = task_id
        self.deadline = deadline
        self.profit = profit

def schedule_jobs(jobs, t):
    profit = 0
    slot = [-1] * t
    jobs.sort(key=lambda x: x.profit, reverse=True)
    for job in jobs:
        for j in reversed(range(job.deadline)):
            if j < t and slot[j] == -1:
                slot[j] = job.task_id
                profit += job.profit
                break

    print("Scheduled jobs are:", list(filter(lambda x: x != -1, slot)))
    print("The total profit:", profit)

if __name__ == "__main__":
    jobs = [
        job(1, 9, 15), job(2, 2, 2), job(3, 5, 18), job(4, 7, 1), job(5, 4, 25), 
        job(6, 2, 20),job(7, 5, 8), job(8, 7, 10), job(9, 4, 12), job(10, 3, 5)
    ]
    t = 15
    schedule_jobs(jobs, t)
