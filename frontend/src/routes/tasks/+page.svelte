<script>
    import { onMount } from 'svelte';
    let tasks = [];

    async function fetchTasks(){
        const res = await fetch('http://127.0.0.1:8000/tasks/');

        if (res.ok){
            tasks = await res.json();
        }else{
            console.error('Failed to fetch task');
        }
    }

    async function deleteTask(id) {
        const res = await fetch(`http://127.0.0.1:8000/tasks/${id}`, {
            method:'DELETE'
        });
        if (res.ok){
            tasks = tasks.filter(task => task.id !== id);
        }else{
            console.error("failed to delete task");
        }
    }
    onMount(fetchTasks);
</script>

<h1 class="text-5xl font-bold">Task List</h1>

{#if tasks.length > 0 }
<div class="overflow-x-auto">
    <table class="table">
        <thead>
            <tr>
                <th></th>
                <th>Title</th>
                <th>Description</th>
                <th>Created On</th>
                <th>Deadline</th>
                <th>Completed</th>
            </tr>
        </thead>
        <tbody>
            {#each tasks as task}
                <tr>
                    <th>{tasks.indexOf(task)+1}</th>
                    <th><a href={`/tasks/${task.id}`} class="btn btn-link">{task.title}</a></th>
                    <th>{task.description.length > 10 ? task.description.slice(0, 10) + '...' : task.description}</th>
                    <th>{task.created_at}</th>
                    <th>{task.deadline}</th>
                    {#if task.completed === false}
                        <th class="text-error">{task.completed}</th>
                    {:else}
                        <th class="text-success">{task.completed}</th>
                    {/if}
                    <th><button class="btn btn-warning" on:click={() => deleteTask(task.id)}>Delete Task</button></th>
                    
                </tr>
            {/each}
        </tbody>
    </table>
</div>
{:else}
    <p class="text-warning">No tasks</p>
{/if}

<a href="tasks/create" class="btn btn-primary">Create New Task</a>

