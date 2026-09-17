# DB2ADMIN.TREPURCHASEORDERTESTDATA

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `PURCHASEORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE`, `GROUPCODE`, `TESTCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 69462

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SELECTED` | SMALLINT | NOT NULL |  |  |  |
| 1 | `PURCHASEORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PURCHASEORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `GROUPCODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `TESTCODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 6 | `GROUPDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 7 | `TESTDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 8 | `SEQUENCEGROUP` | DECIMAL(5,0) |  |  |  |  |
| 9 | `SEQUENCETEST` | DECIMAL(5,0) |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PURCHASEORDER_PURCHASEORDER` | `PURCHASEORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE` | [`PURCHASEORDER`](../PURCHASING/PURCHASEORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `TREPURCHASEORDERTESTDATA.PURCHASEORDERCOMPANYCODE = PURCHASEORDER.COMPANYCODE AND TREPURCHASEORDERTESTDATA.PURCHASEORDERCOUNTERCODE = PURCHASEORDER.COUNTERCODE AND TREPURCHASEORDERTESTDATA.PURCHASEORDERCODE = PURCHASEORDER.CODE` |
| `TREPURCHASEORDERTESTGROUP_GROUP` | `PURCHASEORDERCOMPANYCODE`, `GROUPCODE` | [`TREPURCHASEORDERTESTGROUP`](../PURCHASING/TREPURCHASEORDERTESTGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TREPURCHASEORDERTESTDATA.PURCHASEORDERCOMPANYCODE = TREPURCHASEORDERTESTGROUP.COMPANYCODE AND TREPURCHASEORDERTESTDATA.GROUPCODE = TREPURCHASEORDERTESTGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TREPURCHASEORDERTESTDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SELECTED,
       t.PURCHASEORDERCOMPANYCODE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.GROUPCODE,
       t.TESTCODE,
       t.GROUPDESCRIPTION,
       t.TESTDESCRIPTION,
       t.SEQUENCEGROUP,
       t.SEQUENCETEST,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.TREPURCHASEORDERTESTDATA t
FETCH FIRST 100 ROWS ONLY;
```
