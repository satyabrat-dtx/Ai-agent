# DB2ADMIN.ABSMAILBOXATTACH

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `ABSMAILBOXMAILIDENTIFIER`, `IDENTIFIER`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 34318

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSMAILBOXMAILIDENTIFIER` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `IDENTIFIER` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `ATTACHTYPE` | INTEGER | NOT NULL |  |  |  |
| 3 | `ATTACHMENTABSOUTQUEUENAME` | CHAR(20) |  |  |  |  |
| 4 | `ATTACHMENTSPOOLID` | BIGINT | NOT NULL |  |  |  |
| 5 | `MULTIMEDIAFATHERID` | BIGINT | NOT NULL |  |  |  |
| 6 | `MULTIMEDIAKEY` | CHAR(20) |  |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSMAILBOX_ATTACHMENT` | `ABSMAILBOXMAILIDENTIFIER` | [`ABSMAILBOX`](../PLATFORM/ABSMAILBOX.md) | `MAILIDENTIFIER` | RESTRICT | `ABSMAILBOXATTACH.ABSMAILBOXMAILIDENTIFIER = ABSMAILBOX.MAILIDENTIFIER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSMAILBOXATTACHUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSMAILBOXMAILIDENTIFIER,
       t.IDENTIFIER,
       t.ATTACHTYPE,
       t.ATTACHMENTABSOUTQUEUENAME,
       t.ATTACHMENTSPOOLID,
       t.MULTIMEDIAFATHERID,
       t.MULTIMEDIAKEY,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSMAILBOXATTACH t
FETCH FIRST 100 ROWS ONLY;
```
