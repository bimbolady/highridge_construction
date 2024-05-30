generate_name <- function() {
  first_names <- c('John', 'Jane', 'Alex', 'Emily', 'Chris', 'Katie', 'Mike', 'Laura')
  last_names <- c('Smith', 'Doe', 'Brown', 'Wilson', 'Johnson', 'Lee', 'Walker', 'White')
  paste(sample(first_names, 1), sample(last_names, 1))
}

generate_salary <- function() {
  sample(5000:35000, 1)
}

generate_gender <- function() {
  sample(c('Male', 'Female'), 1)
}

workers <- list()
for (i in 1:400) {
  name <- generate_name()
  salary <- generate_salary()
  gender <- generate_gender()
  workers[[i]] <- list(name = name, salary = salary, gender = gender)
}

for (worker in workers) {
  name <- worker$name
  salary <- worker$salary
  gender <- worker$gender
  employee_level <- ""
  
  tryCatch({
    if (salary > 10000 && salary < 20000) {
      employee_level <- "A1"
    }
    if (salary > 7500 && salary < 30000 && gender == "Female") {
      employee_level <- "A5-F"
    }
    
    cat(sprintf("Name: %s, Salary: %d, Gender: %s, Employee Level: %s\n", name, salary, gender, employee_level))
    
  }, error = function(e) {
    cat(sprintf("Error processing payment slip for %s: %s\n", name, e$message))
  })
}
x <- seq(-pi, pi, 0.1)
plot(x, cos(x))