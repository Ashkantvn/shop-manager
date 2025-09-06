// Profile codes
const profile_grids = document.querySelectorAll(".profile-grid")


profile_grids.forEach(profile_grid=>{
        if (profile_grid.children.length === 1)
            profile_grid.style.gridTemplateColumns= "1fr";
    }
)