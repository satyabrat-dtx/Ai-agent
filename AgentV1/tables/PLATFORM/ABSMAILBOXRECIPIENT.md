# DB2ADMIN.ABSMAILBOXRECIPIENT

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `ABSMAILBOXMAILIDENTIFIER`, `RECIPIENT`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 20436

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSMAILBOXMAILIDENTIFIER` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `RECIPIENTTYPE` | INTEGER | NOT NULL |  |  |  |
| 2 | `RECIPIENT` | CHAR(150) | NOT NULL | PK | primary_key |  |
| 3 | `VALIDSENTADDRESS` | SMALLINT | NOT NULL |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSMAILBOX_MAILRECIPIENT` | `ABSMAILBOXMAILIDENTIFIER` | [`ABSMAILBOX`](../PLATFORM/ABSMAILBOX.md) | `MAILIDENTIFIER` | RESTRICT | `ABSMAILBOXRECIPIENT.ABSMAILBOXMAILIDENTIFIER = ABSMAILBOX.MAILIDENTIFIER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSMAILBOXRECIPIENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSMAILBOXMAILIDENTIFIER,
       t.RECIPIENTTYPE,
       t.RECIPIENT,
       t.VALIDSENTADDRESS,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSMAILBOXRECIPIENT t
FETCH FIRST 100 ROWS ONLY;
```
