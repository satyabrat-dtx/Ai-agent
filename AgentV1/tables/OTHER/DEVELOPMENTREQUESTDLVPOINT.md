# DB2ADMIN.DEVELOPMENTREQUESTDLVPOINT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `DEVELOPMENTREQUESTCOMPANYCODE`, `DEVELOPMENTREQUESTCOUNTERCODE`, `DEVELOPMENTREQUESTCODE`, `ADDRESSUNIQUEID`, `ADDRESSCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 206126

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DEVELOPMENTREQUESTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `DEVELOPMENTREQUESTCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DEVELOPMENTREQUESTCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ADDRESSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 4 | `ADDRESSCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DEVELOPMENTREQUEST_DEVELOPMENTREQUESTDELIVERYPOINT` | `DEVELOPMENTREQUESTCOMPANYCODE`, `DEVELOPMENTREQUESTCOUNTERCODE`, `DEVELOPMENTREQUESTCODE` | [`DEVELOPMENTREQUEST`](../OTHER/DEVELOPMENTREQUEST.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `DEVELOPMENTREQUESTDLVPOINT.DEVELOPMENTREQUESTCOMPANYCODE = DEVELOPMENTREQUEST.COMPANYCODE AND DEVELOPMENTREQUESTDLVPOINT.DEVELOPMENTREQUESTCOUNTERCODE = DEVELOPMENTREQUEST.COUNTERCODE AND DEVELOPMENTREQUESTDLVPOINT.DEVELOPMENTREQUESTCODE = DEVELOPMENTREQUEST.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DEVELOPMENTREQUESTDLVPOINTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DEVELOPMENTREQUESTCOMPANYCODE,
       t.DEVELOPMENTREQUESTCOUNTERCODE,
       t.DEVELOPMENTREQUESTCODE,
       t.ADDRESSUNIQUEID,
       t.ADDRESSCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.DEVELOPMENTREQUESTDLVPOINT t
FETCH FIRST 100 ROWS ONLY;
```
