# DB2ADMIN.PRODUCTPRODUCTIONPRICE

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'PRODUCT')
- **Roles**: `business_data`
- **Columns**: 33
- **Primary key**: `COMPANYCODE`, `ITEMTYPEAFICODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`, `COSTGROUPCODE`, `PLANTCODE`, `QUALITYLEVELCODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 20824

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 3 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 4 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 5 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `COSTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 13 | `PLANTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 14 | `QUALITYLEVELCODE` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 15 | `UNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `SALESPRICE` | DECIMAL(18,5) |  |  |  |  |
| 17 | `PRODUCTIONPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 18 | `COSTELEMENTITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 19 | `COSTELEMENTSUBCODE01` | CHAR(20) |  | FK | foreign_key |  |
| 20 | `COSTCENTERCODE` | CHAR(20) |  | FK | foreign_key |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 26 | `PLANTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 27 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 28 | `COSTELEMENTCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 29 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 31 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 32 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRODUCTPRODUCTIONPRICE.COMPANYCODE = COMPANY.CODE` |
| `COSTCENTER_COSTCENTER` | `COSTCENTERCOMPANYCODE`, `COSTCENTERCODE` | [`COSTCENTER`](../COSTING/COSTCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTPRODUCTIONPRICE.COSTCENTERCOMPANYCODE = COSTCENTER.COMPANYCODE AND PRODUCTPRODUCTIONPRICE.COSTCENTERCODE = COSTCENTER.CODE` |
| `COSTELEMENT_COSTELEMENT` | `COSTELEMENTCOMPANYCODE`, `COSTELEMENTITEMTYPECODE`, `COSTELEMENTSUBCODE01` | [`COSTELEMENT`](../COSTING/COSTELEMENT.md) | `COMPANYCODE`, `ITEMTYPECODE`, `SUBCODE01` | RESTRICT | `PRODUCTPRODUCTIONPRICE.COSTELEMENTCOMPANYCODE = COSTELEMENT.COMPANYCODE AND PRODUCTPRODUCTIONPRICE.COSTELEMENTITEMTYPECODE = COSTELEMENT.ITEMTYPECODE AND PRODUCTPRODUCTIONPRICE.COSTELEMENTSUBCODE01 = COSTELEMENT.SUBCODE01` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTPRODUCTIONPRICE.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND PRODUCTPRODUCTIONPRICE.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `UNITOFMEASURE_UNITOFMEASURE` | `UNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PRODUCTPRODUCTIONPRICE.UNITOFMEASURECODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRODUCTPRODUCTIONPRICEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08,
       t.SUBCODE09,
       t.SUBCODE10
FROM   DB2ADMIN.PRODUCTPRODUCTIONPRICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
