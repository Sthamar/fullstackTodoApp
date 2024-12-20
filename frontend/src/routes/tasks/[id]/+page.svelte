<script lang="ts">
    // Receiving data from the server or parent component
    export let data;

    // Initialize local variables for task properties
    let updatedTitle = data.title;
    let updatedDescription = data.description;
    let updatedDeadline = data.deadline;
    let updatedCompleted = data.completed;

    // Function to handle task updates
    async function updateTask(event: Event) {
        event.preventDefault(); // Prevent default form submission

        const updatedTask = {
            title: updatedTitle,
            description: updatedDescription,
            deadline: updatedDeadline,
            completed: updatedCompleted
        };

        try {
            // Send PUT request to update the task
            const res = await fetch(`http://127.0.0.1:8000/tasks/${data.id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(updatedTask)
            });

            if (!res.ok) {
                throw new Error(`Failed to update task. Status: ${res.status}`);
            }

            const resBody = await res.json();
            alert(`Task updated successfully: ${resBody.title}`);

        } catch (error) {
            console.error(error.message);
            alert('An error occurred while updating the task. Please try again.');
        }
    }
</script>

<h1 class="text-5xl font-bold">Edit Task</h1>
<form class="card-body" on:submit={updateTask}>
    <div class="form-control">
        <input 
            type="text" 
            bind:value={updatedTitle} 
            class="input input-bordered input-primary w-full max-w-xs" 
            placeholder="Title"
        />
    </div>
    <div class="form-control">
        <textarea 
            bind:value={updatedDescription} 
            class="textarea textarea-primary" 
            placeholder="Description"
        ></textarea>
    </div>
    <div class="form-control">
        <input 
            type="date" 
            bind:value={updatedDeadline} 
            class="input input-bordered input-primary w-full max-w-xs" 
            placeholder="Deadline"
        />
    </div>
    <div class="form-control">
        <label class="label cursor-pointer">
            <span class="label-text">Completed</span>
            <input 
                type="checkbox" 
                bind:checked={updatedCompleted} 
                class="checkbox checkbox-primary"
            />
        </label>
    </div>
    <button type="submit" class="btn btn-secondary">Update</button>
</form>
