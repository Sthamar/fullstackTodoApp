<script>
    import "tailwindcss/tailwind.css";
    import { page } from '$app/stores';

    $: isTaskPage = $page.url.pathname.startsWith('/tasks');
    
    let theme = 'retro';
    function switchTheme(newTheme) {
    theme = newTheme;
    document.documentElement.setAttribute('data-theme', newTheme);
  }
    let nav_list = [
        {"item":"Home",'link':'/'},
        {"item":"Task",'link':'/tasks'},
    ]


</script>
  
<div class="navbar bg-base-100 fixed">
    <div class="flex-1">
        <a href="/" class="btn btn-ghost text-xl">Todo</a>
    </div>
    <div class="flex-none">
        <ul class="menu menu-horizontal px-1">
            {#each nav_list as nav}
                <li><a href= {nav.link}>{nav.item}</a></li>
            {/each}

        </ul>
    </div>
    
</div>

<div class="hero bg-base-200 min-h-screen">
    <div class="hero-content text-center">
        <div class={isTaskPage ? 'max-w-4xl' : 'max-w-md'}>
            <slot />
        </div>
    </div>
</div>
