# DB2ADMIN.BILLOFEXCHANGECHECKLIST

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 1 of 1 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `BILLOFEXCHANGECOMPANYCODE`, `BILLOFEXCHANGEDIVISIONCODE`, `BILLOFEXCHANGECODE`, `CLCODEUSERGENERICGROUPTYPECODE`, `CLCODECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 182048

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BILLOFEXCHANGECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `BILLOFEXCHANGEDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `BILLOFEXCHANGECODE` | CHAR(12) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CLCODUSGENGRPTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `CLCODEUSERGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `CLCODECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 7 | `REASON` | VARCHAR(255) |  |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BILLOFEXCHANGE_CHECKLIST` | `BILLOFEXCHANGECOMPANYCODE`, `BILLOFEXCHANGEDIVISIONCODE`, `BILLOFEXCHANGECODE` | [`BILLOFEXCHANGE`](../FINANCE/BILLOFEXCHANGE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `BILLOFEXCHANGECHECKLIST.BILLOFEXCHANGECOMPANYCODE = BILLOFEXCHANGE.COMPANYCODE AND BILLOFEXCHANGECHECKLIST.BILLOFEXCHANGEDIVISIONCODE = BILLOFEXCHANGE.DIVISIONCODE AND BILLOFEXCHANGECHECKLIST.BILLOFEXCHANGECODE = BILLOFEXCHANGE.CODE` |
| `USERGENERICGROUP_CLCODE` | `CLCODUSGENGRPTYPECOMPANYCODE`, `CLCODEUSERGENERICGROUPTYPECODE`, `CLCODECODE` | [`USERGENERICGROUP`](../CORE_MASTER/USERGENERICGROUP.md) | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE`, `CODE` | RESTRICT | `BILLOFEXCHANGECHECKLIST.CLCODUSGENGRPTYPECOMPANYCODE = USERGENERICGROUP.USERGENGROUPTYPECOMPANYCODE AND BILLOFEXCHANGECHECKLIST.CLCODEUSERGENERICGROUPTYPECODE = USERGENERICGROUP.USERGENERICGROUPTYPECODE AND BILLOFEXCHANGECHECKLIST.CLCODECODE = USERGENERICGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BILLOFEXCHANGECHECKLISTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.BILLOFEXCHANGECOMPANYCODE,
       t.BILLOFEXCHANGEDIVISIONCODE,
       t.BILLOFEXCHANGECODE,
       t.CLCODUSGENGRPTYPECOMPANYCODE,
       t.CLCODEUSERGENERICGROUPTYPECODE,
       t.CLCODECODE,
       t.REMARK,
       t.REASON,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.BILLOFEXCHANGECHECKLIST t
FETCH FIRST 100 ROWS ONLY;
```
