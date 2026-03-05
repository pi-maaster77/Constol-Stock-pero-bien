// frontend/src/types/notifications.ts

export type NotificationType =
    | 'stock_in'
    | 'stock_out'
    | 'stock_transfer'
    | 'stock_low'
    | 'stock_critical'
    | 'stock_adjustment'
    | 'expires_soon'
    | 'expired'
    | 'operation_error'
    | 'operation_success'
    | 'error'
    | 'success'