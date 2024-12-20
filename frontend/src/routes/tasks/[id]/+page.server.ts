import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = async (event) => {
    const { id } = event.params;
    console.log({id}); 


    const res = await fetch(`http://127.0.0.1:8000/tasks/${id}`);
    
    if (!res.ok) {
        throw new Error('Failed to fetch task');
    }

    const responseBody = await res.json();

    console.log(responseBody);  

    return {
        id:id,
        title: responseBody.title,
        description: responseBody.description,  
        deadline: responseBody.deadline,
        completed: responseBody.completed
    };
};
