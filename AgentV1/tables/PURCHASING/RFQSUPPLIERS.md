# DB2ADMIN.RFQSUPPLIERS

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `RFQHEADERCOMPANYCODE`, `RFQHEADERCOUNTERCODE`, `RFQHEADERCODE`, `LINENO`, `ORDPRNCUSTOMERSUPPLIERTYPE`, `ORDPRNCUSTOMERSUPPLIERCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 109676

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RFQHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `RFQHEADERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `RFQHEADERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 5 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 6 | `LEGALNAME` | VARCHAR(200) |  |  |  |  |
| 7 | `READFLAG` | SMALLINT | NOT NULL |  |  |  |
| 8 | `QUOTATIONCREATED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 11 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DIVISION_DIVISION` | `RFQHEADERCOMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RFQSUPPLIERS.RFQHEADERCOMPANYCODE = DIVISION.COMPANYCODE AND RFQSUPPLIERS.DIVISIONCODE = DIVISION.CODE` |
| `RFQHEADER_LINESUPPLIER` | `RFQHEADERCOMPANYCODE`, `RFQHEADERCOUNTERCODE`, `RFQHEADERCODE` | [`RFQHEADER`](../PURCHASING/RFQHEADER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `RFQSUPPLIERS.RFQHEADERCOMPANYCODE = RFQHEADER.COMPANYCODE AND RFQSUPPLIERS.RFQHEADERCOUNTERCODE = RFQHEADER.COUNTERCODE AND RFQSUPPLIERS.RFQHEADERCODE = RFQHEADER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RFQSUPPLIERSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RFQHEADERCOMPANYCODE,
       t.RFQHEADERCOUNTERCODE,
       t.RFQHEADERCODE,
       t.LINENO,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.LEGALNAME,
       t.READFLAG,
       t.QUOTATIONCREATED,
       t.ABSUNIQUEID,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS
FROM   DB2ADMIN.RFQSUPPLIERS t
FETCH FIRST 100 ROWS ONLY;
```
