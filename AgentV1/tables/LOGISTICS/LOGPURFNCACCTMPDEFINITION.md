# DB2ADMIN.LOGPURFNCACCTMPDEFINITION

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 54
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 113418

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 2 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 3 | `INITIALDATE` | DATE |  |  |  |  |
| 4 | `FINALDATE` | DATE |  |  |  |  |
| 5 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 6 | `LINETYPE` | CHAR(1) |  |  |  |  |
| 7 | `CREDITNOTE` | SMALLINT | NOT NULL |  |  |  |
| 8 | `ACCOUNTTEMPLATECODE` | CHAR(6) |  |  |  |  |
| 9 | `ELECTINVACCOUNTTEMPLATECODE` | CHAR(6) |  |  |  |  |
| 10 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 11 | `ORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 12 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 13 | `ORDPRNGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 14 | `ORDERPARTNERGROUPCODE` | CHAR(3) |  |  |  |  |
| 15 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 16 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 17 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 18 | `ORDERLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 19 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 21 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 22 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 32 | `ORDITEMGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 33 | `ORDERITEMGROUPCODE` | CHAR(3) |  |  |  |  |
| 34 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 35 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 36 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 37 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 38 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 39 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 40 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 41 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 42 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 43 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 44 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 45 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 46 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 47 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 48 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 49 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 50 | `RFPARTNERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 51 | `RFPRNGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 52 | `REFERENCEPARTNERGROUPCODE` | CHAR(3) |  |  |  |  |
| 53 | `PROTOTYPEMANAGED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPURFNCACCTMPDEFINITION.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NUMBERID,
       t.ORDERTYPE,
       t.INITIALDATE,
       t.FINALDATE,
       t.TEMPLATECODE,
       t.LINETYPE,
       t.CREDITNOTE,
       t.ACCOUNTTEMPLATECODE,
       t.ELECTINVACCOUNTTEMPLATECODE,
       t.DIVISIONCODE,
       t.ORDERTEMPLATECODE
FROM   DB2ADMIN.LOGPURFNCACCTMPDEFINITION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
