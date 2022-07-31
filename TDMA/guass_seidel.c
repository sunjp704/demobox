    N = length(b);
    conv = 0;
    for iter=1:maxsteps
        diffe = 0;
        for i=1:N
            switch i
                case 1
                    ind = 2:N;
                case N
                    ind = 1:N-1;
                otherwise
                    ind = [1:i-1,i+1:N];
            end
            phi_n =(b(i)-dot(A(i,ind),phi(ind)))/A(i,i);
            diffe = max(diffe,abs((phi_n-phi(i))/(phi_n + eps)));
            phi(i)=phi_n;
        end
        if diffe < criteria
            conv = 1;
            fprintf('Converged at step %d.\n',iter);
            fprintf('Maximum normalized difference is  %.2E\n',diffe);
            break;
        end
    end
    if not(conv)
        fprintf('Couldn''t converge within %d iterations\n',iter);
        fprintf('Maximum normalized difference is  %.2E\n',diffe);
    end