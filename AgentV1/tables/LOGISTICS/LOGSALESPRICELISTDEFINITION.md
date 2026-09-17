# DB2ADMIN.LOGSALESPRICELISTDEFINITION

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 46
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 116557

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
| 9 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 10 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 11 | `ORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 12 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `AREACODE` | CHAR(3) |  |  |  |  |
| 14 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 15 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 16 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 17 | `AGENTCODE` | CHAR(3) |  |  |  |  |
| 18 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 19 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 20 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 21 | `ORDERPARTNERBRANDCODE` | CHAR(8) |  |  |  |  |
| 22 | `FNCORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 23 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 24 | `ORDPRNGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 25 | `ORDERPARTNERGROUPCODE` | CHAR(3) |  |  |  |  |
| 26 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 27 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 28 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 30 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 31 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 32 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 33 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 34 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 35 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 36 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 37 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 38 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 39 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 40 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 41 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 42 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 43 | `RFPARTNERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 44 | `RFPRNGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 45 | `REFERENCEPARTNERGROUPCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGSALESPRICELISTDEFINITION.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

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
       t.CURRENCYCODE,
       t.DISCOUNTCATEGORYCODE,
       t.ORDERTEMPLATECODE
FROM   DB2ADMIN.LOGSALESPRICELISTDEFINITION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
