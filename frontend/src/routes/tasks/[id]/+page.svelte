
<script lang="ts">
    let data = $props();

    let task = data.data
    console.log(task)

    let updatedTitle = task.title;
    let updatedDescription = task.description;
    let updatedDeadline = task.deadline;
    let updatedCompleted = task.completed;


    async function updateTask() {
        const updatedTask = {
            title: updatedTitle,
            description: updatedDescription,
            deadline: updatedDeadline,
            completed: updatedCompleted
        };

        // Send PUT request to update the task
        const res = await fetch(`http://127.0.0.1:8000/tasks/${task.id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(updatedTask)
        });

        const resb = await res.json();
        alert(resb.title)

        if (res.ok) {
            alert('Task updated successfully!');
            // You can redirect or update the UI here if needed
        } else {
            console.error('Failed to update task');
        }
    }
    
</script>


    <h1 class="text-5xl font-bold"> Edit Task</h1>
    <form  class="card-body" on:submit={updateTask}>
        <div class="form-control">
            <input type="text" bind:value={updatedTitle} class="input input-bordered input-primary w-full max-w-xs">
        </div>
        <div class="form-control">
            <textarea bind:value={updatedDescription} class="textarea textarea-primary"></textarea>
        </div>
        <div class="form-control">
            <input type="date" bind:value={updatedDeadline} class="input input-bordered input-primary w-full max-w-xs">
        </div>
        <div class="form-control">
            <label class="label cursor-pointer">
            <span class="label-text">Completed</span>
            <input type="checkbox" bind:checked={updatedCompleted} class="checkbox checkbox-primary">
            </label>
        </div>
        <button type="submit" class="btn btn-secondary">Update</button>
    </form>

    <!-- <span class="loading loading-ring loading-lg"></span>
{/if} -->
 
