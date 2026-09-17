# DB2ADMIN.USASTACCOUNTINGDEFINITION

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 36
- **Primary key**: `COMPANYCODE`, `STOCKTRANSACTIONTEMPLATECODE`, `ACCOUNTINGTEMPLATETEMPLATECODE`, `ITEMTYPECODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`, `LOGICALWAREHOUSECODE`, `ARTICLEGROUPCODE`, `QUALITYLEVEL`, `ORDERTEMPLATE`, `CUSTOMERSUPPLIER`, `COSTCENTERCODE`, `COSTCENTERGROUPGROUPCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 107921

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `STOCKTRNTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `STOCKTRANSACTIONTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ACCOUNTINGTEMPLATETEMPLATECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 14 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 15 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 16 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 17 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 18 | `ARTICLEGROUPCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 19 | `QUALITYLEVEL` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 20 | `ORDERTEMPLATE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 21 | `CUSTOMERSUPPLIER` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 22 | `COSTCENTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 23 | `COSTCENTERCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 24 | `COSTCENTERGROUPGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 25 | `ACCOUNTCODED` | CHAR(20) | NOT NULL |  |  |  |
| 26 | `ACCOUNTCODEC` | CHAR(20) | NOT NULL |  |  |  |
| 27 | `VALUATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 28 | `DOCUMENTCLASS` | CHAR(2) |  |  |  |  |
| 29 | `ACCOUNTINGTYPECREDIT` | CHAR(2) |  |  |  |  |
| 30 | `ACCOUNTINGTYPEDEBIT` | CHAR(2) |  |  |  |  |
| 31 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 32 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 33 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 34 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 35 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `USASTACCOUNTINGDEFINITION.COMPANYCODE = COMPANY.CODE` |
| `STOCKTRANSACTIONTEMPLATE_STOCKTRANSACTIONTEMPLATE` | `STOCKTRNTEMPLATECOMPANYCODE`, `STOCKTRANSACTIONTEMPLATECODE` | [`STOCKTRANSACTIONTEMPLATE`](../INVENTORY/STOCKTRANSACTIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `USASTACCOUNTINGDEFINITION.STOCKTRNTEMPLATECOMPANYCODE = STOCKTRANSACTIONTEMPLATE.COMPANYCODE AND USASTACCOUNTINGDEFINITION.STOCKTRANSACTIONTEMPLATECODE = STOCKTRANSACTIONTEMPLATE.CODE` |
| `USASTACCOUNTINGTEMPLATE_ACCOUNTINGTEMPLATE` | `COMPANYCODE`, `ACCOUNTINGTEMPLATETEMPLATECODE` | [`USASTACCOUNTINGTEMPLATE`](../LOCALIZATION/USASTACCOUNTINGTEMPLATE.md) | `COMPANYCODE`, `TEMPLATECODE` | RESTRICT | `USASTACCOUNTINGDEFINITION.COMPANYCODE = USASTACCOUNTINGTEMPLATE.COMPANYCODE AND USASTACCOUNTINGDEFINITION.ACCOUNTINGTEMPLATETEMPLATECODE = USASTACCOUNTINGTEMPLATE.TEMPLATECODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USASTACCOUNTINGDEFINITIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.STOCKTRNTEMPLATECOMPANYCODE,
       t.STOCKTRANSACTIONTEMPLATECODE,
       t.ACCOUNTINGTEMPLATETEMPLATECODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06
FROM   DB2ADMIN.USASTACCOUNTINGDEFINITION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
