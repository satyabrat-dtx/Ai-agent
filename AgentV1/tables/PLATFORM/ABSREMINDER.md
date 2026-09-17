# DB2ADMIN.ABSREMINDER

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `COMPANYCODE`, `USERUSERID`, `IDENTIFIER`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 29071

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `USERUSERID` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `IDENTIFIER` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 3 | `SENDER` | CHAR(50) |  |  |  |  |
| 4 | `SENDINGDATE` | BIGINT | NOT NULL |  |  |  |
| 5 | `DATA` | CLOB(1000000) |  |  |  |  |
| 6 | `ALREADYREAD` | SMALLINT | NOT NULL |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 8 | `NOTIFICATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 9 | `SOURCE` | VARCHAR(250) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUSERDEF_USER` | `USERUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `ABSREMINDER.USERUSERID = ABSUSERDEF.USERID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSREMINDERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.USERUSERID,
       t.IDENTIFIER,
       t.SENDER,
       t.SENDINGDATE,
       t.DATA,
       t.ALREADYREAD,
       t.ABSUNIQUEID,
       t.NOTIFICATIONTYPE,
       t.SOURCE
FROM   DB2ADMIN.ABSREMINDER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
