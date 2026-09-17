# DB2ADMIN.TREWRKPURCHASEORDERTESTDATA

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`, `PURCHASEORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE`, `GROUPCODE`, `TESTCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 69655

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CHOICE` | SMALLINT | NOT NULL |  |  |  |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 3 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `PURCHASEORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `PURCHASEORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `GROUPCODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 8 | `TESTCODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 9 | `TESTDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 10 | `SEQUENCEGROUP` | DECIMAL(5,0) |  |  |  |  |
| 11 | `SEQUENCETEST` | DECIMAL(5,0) |  |  |  |  |
| 12 | `TESTEXIST` | SMALLINT | NOT NULL |  |  |  |
| 13 | `ERRORTEST` | SMALLINT | NOT NULL |  |  |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PURCHASEORDER_PURCHASEORDER` | `PURCHASEORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE` | [`PURCHASEORDER`](../PURCHASING/PURCHASEORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `TREWRKPURCHASEORDERTESTDATA.PURCHASEORDERCOMPANYCODE = PURCHASEORDER.COMPANYCODE AND TREWRKPURCHASEORDERTESTDATA.PURCHASEORDERCOUNTERCODE = PURCHASEORDER.COUNTERCODE AND TREWRKPURCHASEORDERTESTDATA.PURCHASEORDERCODE = PURCHASEORDER.CODE` |
| `TREPURCHASEORDERTESTGROUP_GROUP` | `PURCHASEORDERCOMPANYCODE`, `GROUPCODE` | [`TREPURCHASEORDERTESTGROUP`](../PURCHASING/TREPURCHASEORDERTESTGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TREWRKPURCHASEORDERTESTDATA.PURCHASEORDERCOMPANYCODE = TREPURCHASEORDERTESTGROUP.COMPANYCODE AND TREWRKPURCHASEORDERTESTDATA.GROUPCODE = TREPURCHASEORDERTESTGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TREWRKPURORDERTESTDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CHOICE,
       t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.PURCHASEORDERCOMPANYCODE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.GROUPCODE,
       t.TESTCODE,
       t.TESTDESCRIPTION,
       t.SEQUENCEGROUP,
       t.SEQUENCETEST
FROM   DB2ADMIN.TREWRKPURCHASEORDERTESTDATA t
FETCH FIRST 100 ROWS ONLY;
```
