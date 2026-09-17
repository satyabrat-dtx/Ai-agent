# DB2ADMIN.EXPORTENVIRONMENT

- **Module**: `PDM` (low confidence — FK neighbourhood: 1 of 1 related tables are PDM)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `CODE`
- **FK degree**: referenced by 4 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 14004

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `DESCRIPTION` | CHAR(50) | NOT NULL |  | description |  |
| 2 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 3 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 4 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 5 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 6 | `PHYSICALDELETE` | CHAR(1) |  |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 4

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `EXPORTENVIRONMENT_ENVIRONMENT` | [`ADTOEXPORT`](../OTHER/ADTOEXPORT.md) | `ENVIRONMENTCODE` | `ADTOEXPORT.ENVIRONMENTCODE = EXPORTENVIRONMENT.CODE` |
| `EXPORTENVIRONMENT_ENVIRONMENT` | [`EXPORTENTITY`](../PDM/EXPORTENTITY.md) | `ENVIRONMENTCODE` | `EXPORTENTITY.ENVIRONMENTCODE = EXPORTENVIRONMENT.CODE` |
| `EXPORTENVIRONMENT_EXPORTENVIRONMENT` | [`PDMCUSTOMIZEDOPTIONS`](../PDM/PDMCUSTOMIZEDOPTIONS.md) | `EXPORTENVIRONMENTCODE` | `PDMCUSTOMIZEDOPTIONS.EXPORTENVIRONMENTCODE = EXPORTENVIRONMENT.CODE` |
| `EXPORTENVIRONMENT_ENVIRONMENT` | [`QAEXPORTENTITY`](../PDM/QAEXPORTENTITY.md) | `ENVIRONMENTCODE` | `QAEXPORTENTITY.ENVIRONMENTCODE = EXPORTENVIRONMENT.CODE` |

## Indexes

- `EXPORTENVIRONMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.DESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.PHYSICALDELETE,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.EXPORTENVIRONMENT t
FETCH FIRST 100 ROWS ONLY;
```
