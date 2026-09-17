# DB2ADMIN.LOGPURCHASEPRICELIST

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 43
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 116933

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `CODE` | CHAR(8) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `TEMPLATEDEFINITIONTYPE` | CHAR(1) |  |  |  |  |
| 5 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 6 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 7 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 8 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 9 | `INITIALDATE` | DATE |  |  |  |  |
| 10 | `FINALDATE` | DATE |  |  |  |  |
| 11 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 12 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 13 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 14 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 15 | `MAXPOSITIVEPRCFOREXCHANGERATE` | DECIMAL(5,2) |  |  |  |  |
| 16 | `MAXNEGATIVEPRCFOREXCHANGERATE` | DECIMAL(5,2) |  |  |  |  |
| 17 | `ALLOWDIFFERENCES` | SMALLINT | NOT NULL |  |  |  |
| 18 | `MAXPOSITIVEPRCFORDOCPRICE` | DECIMAL(5,2) |  |  |  |  |
| 19 | `MAXNEGATIVEPRCFORDOCPRICE` | DECIMAL(5,2) |  |  |  |  |
| 20 | `ALLOWCONVERSION` | SMALLINT | NOT NULL |  |  |  |
| 21 | `ORDERCATEGORYORDERTYPE` | CHAR(1) |  |  |  |  |
| 22 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 23 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 25 | `ORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 26 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 27 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 28 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
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

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPURCHASEPRICELIST.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.TEMPLATEDEFINITIONTYPE,
       t.TEMPLATECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.INITIALDATE,
       t.FINALDATE,
       t.ORDPRNCUSTOMERSUPPLIERTYPE
FROM   DB2ADMIN.LOGPURCHASEPRICELIST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
