# DB2ADMIN.TRNUMBERINGSUBSERIES

- **Module**: `WAREHOUSE` (low confidence — FK neighbourhood: 1 of 1 related tables are WAREHOUSE)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `TRANSACTIONALNUMBERINGCMYCODE`, `TRANSACTIONALNUMBERINGCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 18827

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TRANSACTIONALNUMBERINGCMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TRANSACTIONALNUMBERINGCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CODE` | CHAR(30) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `LASTUSEDNUMBER` | DECIMAL(15,0) | NOT NULL |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TRNUMBERINGSUBSERIES.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `TRANSACTIONALNUMBERING_SUBSERIES` | `TRANSACTIONALNUMBERINGCMYCODE`, `TRANSACTIONALNUMBERINGCODE` | [`TRANSACTIONALNUMBERING`](../WAREHOUSE/TRANSACTIONALNUMBERING.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TRNUMBERINGSUBSERIES.TRANSACTIONALNUMBERINGCMYCODE = TRANSACTIONALNUMBERING.COMPANYCODE AND TRNUMBERINGSUBSERIES.TRANSACTIONALNUMBERINGCODE = TRANSACTIONALNUMBERING.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TRNUMBERINGSUBSERIESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TRANSACTIONALNUMBERINGCMYCODE,
       t.TRANSACTIONALNUMBERINGCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.LASTUSEDNUMBER,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.OWNINGCOMPANYCODE
FROM   DB2ADMIN.TRNUMBERINGSUBSERIES t
FETCH FIRST 100 ROWS ONLY;
```
