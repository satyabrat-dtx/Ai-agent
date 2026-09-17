# DB2ADMIN.LOGSALESPRICEDEFINITION

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 63
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 116426

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 2 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 3 | `INITIALDATE` | DATE |  |  |  |  |
| 4 | `FINALDATE` | DATE |  |  |  |  |
| 5 | `TEMPLATEDEFINITIONTYPE` | CHAR(1) |  |  |  |  |
| 6 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 8 | `PRICELISTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `COMPOUNDPRICEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `BREAKDOWNTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 12 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 13 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 14 | `ORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 15 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 16 | `AREACODE` | CHAR(3) |  |  |  |  |
| 17 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 18 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 19 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 20 | `AGENTCODE` | CHAR(3) |  |  |  |  |
| 21 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 23 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 24 | `ORDERPARTNERBRANDCODE` | CHAR(8) |  |  |  |  |
| 25 | `FNCORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 26 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 27 | `ORDPRNGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 28 | `ORDERPARTNERGROUPCODE` | CHAR(3) |  |  |  |  |
| 29 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 30 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 32 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 33 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 34 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 35 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 39 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 40 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 41 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 42 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 43 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 44 | `ORDITEMGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 45 | `ORDERITEMGROUPCODE` | CHAR(3) |  |  |  |  |
| 46 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 47 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 48 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 49 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 50 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 51 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 52 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 53 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 54 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 55 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 56 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 57 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 58 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 59 | `RFPARTNERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 60 | `RFPRNGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 61 | `REFERENCEPARTNERGROUPCODE` | CHAR(3) |  |  |  |  |
| 62 | `PROTOTYPEMANAGED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGSALESPRICEDEFINITION.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGSALESPRICEDEFINITIONDETAIL`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NUMBERID,
       t.ORDERTYPE,
       t.INITIALDATE,
       t.FINALDATE,
       t.TEMPLATEDEFINITIONTYPE,
       t.TEMPLATECODE,
       t.PRICELISTCODE,
       t.PRICELISTTYPE,
       t.COMPOUNDPRICEREQUIRED,
       t.BREAKDOWNTYPE,
       t.UNITOFMEASURECODE
FROM   DB2ADMIN.LOGSALESPRICEDEFINITION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
