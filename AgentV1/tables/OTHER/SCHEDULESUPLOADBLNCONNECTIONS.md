# DB2ADMIN.SCHEDULESUPLOADBLNCONNECTIONS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 42510

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `USED` | SMALLINT | NOT NULL |  |  |  |
| 3 | `COUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 4 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 6 | `SUBSTEP` | INTEGER | NOT NULL |  |  |  |
| 7 | `REPROCESS` | INTEGER | NOT NULL |  |  |  |
| 8 | `TOBEPROCESSED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `COUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SCHEDULESUPLOADBLNCONNECTIONS.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND SCHEDULESUPLOADBLNCONNECTIONS.COUNTERCODE = COUNTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EDULESUPLOADBLNCONNECTIONSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NUMBERID,
       t.USED,
       t.COUNTERCODE,
       t.CODE,
       t.STEPNUMBER,
       t.SUBSTEP,
       t.REPROCESS,
       t.TOBEPROCESSED,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.SCHEDULESUPLOADBLNCONNECTIONS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
