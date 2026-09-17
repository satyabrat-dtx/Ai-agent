# DB2ADMIN.PRODUCTIONBOOKINGSHEETHEADER

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `business_data`
- **Columns**: 31
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `PRDORDERCODE`, `OBNOOBNUMBER`, `TRANSACTIONDATE`, `SHIFT`
- **FK degree**: referenced by 1 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 127392

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TRANSACTIONDATE` | DATE | NOT NULL | PK | primary_key |  |
| 2 | `TRANSACTIONTIME` | TIME | NOT NULL |  |  |  |
| 3 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 4 | `OBNOOBNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 5 | `PRDORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 6 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 9 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `TARGET` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 19 | `MACHINENOCODE` | CHAR(8) |  | FK | foreign_key |  |
| 20 | `SHIFT` | INTEGER | NOT NULL | PK | primary_key |  |
| 21 | `SHIFTOPTION` | CHAR(2) |  |  |  |  |
| 22 | `PERHOUR` | CHAR(2) |  |  |  |  |
| 23 | `PERTWOHOUR` | CHAR(2) |  |  |  |  |
| 24 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 25 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 26 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 27 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 28 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 29 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRODUCTIONBOOKINGSHEETHEADER.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONBOOKINGSHEETHEADER.COMPANYCODE = DIVISION.COMPANYCODE AND PRODUCTIONBOOKINGSHEETHEADER.DIVISIONCODE = DIVISION.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONBOOKINGSHEETHEADER.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND PRODUCTIONBOOKINGSHEETHEADER.ITEMTYPECODE = ITEMTYPE.CODE` |
| `RESOURCES_MACHINENO` | `COMPANYCODE`, `MACHINENOCODE` | [`RESOURCES`](../PRODUCTION/RESOURCES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONBOOKINGSHEETHEADER.COMPANYCODE = RESOURCES.COMPANYCODE AND PRODUCTIONBOOKINGSHEETHEADER.MACHINENOCODE = RESOURCES.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PRODUCTIONBOOKINGSHEETHEADER_LINE` | [`PRODUCTIONBOOKINGSHEETDETAIL`](../PRODUCTION/PRODUCTIONBOOKINGSHEETDETAIL.md) | `PROBSHEETHEADERCOMPANYCODE`, `PROBSHEETHEADERDIVISIONCODE`, `PROBSHEETHEADERPRDORDERCODE`, `PROBSHEETHEADEROBNOOBNUMBER`, `PROBSHEADERTRANSACTIONDATE`, `PROBOOKINGSHEETHEADERSHIFT` | `PRODUCTIONBOOKINGSHEETDETAIL.PROBSHEETHEADERCOMPANYCODE = PRODUCTIONBOOKINGSHEETHEADER.COMPANYCODE AND PRODUCTIONBOOKINGSHEETDETAIL.PROBSHEETHEADERDIVISIONCODE = PRODUCTIONBOOKINGSHEETHEADER.DIVISIONCODE AND PRODUCTIONBOOKINGSHEETDETAIL.PROBSHEETHEADERPRDORDERCODE = PRODUCTIONBOOKINGSHEETHEADER.PRDORDERCODE AND PRODUCTIONBOOKINGSHEETDETAIL.PROBSHEETHEADEROBNOOBNUMBER = PRODUCTIONBOOKINGSHEETHEADER.OBNOOBNUMBER AND PRODUCTIONBOOKINGSHEETDETAIL.PROBSHEADERTRANSACTIONDATE = PRODUCTIONBOOKINGSHEETHEADER.TRANSACTIONDATE AND PRODUCTIONBOOKINGSHEETDETAIL.PROBOOKINGSHEETHEADERSHIFT = PRODUCTIONBOOKINGSHEETHEADER.SHIFT` |

## Indexes

- `PROBOOKINGSHEETHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TRANSACTIONDATE,
       t.TRANSACTIONTIME,
       t.DIVISIONCODE,
       t.OBNOOBNUMBER,
       t.PRDORDERCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04
FROM   DB2ADMIN.PRODUCTIONBOOKINGSHEETHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
