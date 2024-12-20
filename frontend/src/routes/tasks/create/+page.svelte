<script>
    let title = '';
    let description = '';
    let deadline = '';


    async function createTask(){
        const res = await fetch("http://127.0.0.1:8000/tasks/",{
            method: 'POST',
            headers: {'content-Type': 'application/json'},
            body: JSON.stringify({
                title,
                description,
                deadline,
                completed: false
            })
        });

        if (res.ok){
            window.location.href = '/tasks';

        }else{
            alert("faild to create task");

        }
    }
</script>
<h1 class="text-5xl font-bold">Create Task</h1>
<form on:submit|preventDefault={createTask} class="card-body">
    <div class="form-control">
        <input type="text" placeholder="Title" bind:value={title} class="input input-bordered input-primary w-full max-w-xs"/>
    </div>
    <div class="form-control">
    <textarea bind:value={description} class="textarea textarea-primary" placeholder="Description"></textarea>
    </div>
    <div class="form-control">
    <input type="date" bind:value={deadline} class=" input input-bordered input-primary w-full max-w-xs"/>
    </div>
    <div class="form-control mt-6">
        <button type="submit" class="btn btn-primary ">Create</button>
    </div>
</form>