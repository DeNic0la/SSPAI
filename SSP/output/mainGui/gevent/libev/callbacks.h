struct ev_loop;
struct PyGeventLoopObject;
struct PyGeventCallbackObject;

#define DEFINE_CALLBACK(WATCHER_LC, WATCHER_TYPE) \
    void gevent_callback_##WATCHER_LC(struct ev_loop *, void *, int);


#define DEFINE_CALLBACKS0              \
    DEFINE_CALLBACK(io, IO);           \
    DEFINE_CALLBACK(timer, Timer);     \
    DEFINE_CALLBACK(signal, Signal);   \
    DEFINE_CALLBACK(idle, Idle);       \
    DEFINE_CALLBACK(prepare, Prepare); \
    DEFINE_CALLBACK(check, Check);     \
    DEFINE_CALLBACK(fork, Fork);       \
    DEFINE_CALLBACK(async, Async);     \
    DEFINE_CALLBACK(stat, Stat);       \
    DEFINE_CALLBACK(child, Child);


#define DEFINE_CALLBACKS DEFINE_CALLBACKS0


DEFINE_CALLBACKS


void gevent_run_callbacks(struct ev_loop *, void *, int);



void gevent_call(struct PyGeventLoopObject* loop, struct PyGeventCallbackObject* cb);

static void gevent_noop(struct ev_loop *_loop, void *watcher, int revents) {
}

/* Only used on Win32 */
void gevent_periodic_signal_check(struct ev_loop *, void *, int);
