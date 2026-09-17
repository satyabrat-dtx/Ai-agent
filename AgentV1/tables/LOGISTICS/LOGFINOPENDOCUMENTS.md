# DB2ADMIN.LOGFINOPENDOCUMENTS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 50
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 225151

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSVERSIONNUMBER` | BIGINT | NOT NULL |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL |  |  |  |
| 3 | `FINANCIALYEARCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `FINANCIALYEARCODE` | DECIMAL(4,0) | NOT NULL |  |  |  |
| 5 | `DOCUMENTTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `DOCUMENTTEMPLATECODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 8 | `STATISTICALGROUPCODE` | CHAR(6) | NOT NULL |  |  |  |
| 9 | `DOCUMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 11 | `LINENUMBER` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 12 | `CREDITLINE` | SMALLINT | NOT NULL |  |  |  |
| 13 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 14 | `ORDERPARTNERTYPE` | CHAR(1) |  |  |  |  |
| 15 | `ORDERPARTNERCODE` | CHAR(8) |  |  |  |  |
| 16 | `GLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 17 | `GLCODE` | CHAR(20) |  |  |  |  |
| 18 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 19 | `UNDERPROPOSAL` | SMALLINT | NOT NULL |  |  |  |
| 20 | `UNDERLCPAYMENT` | SMALLINT | NOT NULL |  |  |  |
| 21 | `POSTINGDATE` | DATE | NOT NULL |  |  |  |
| 22 | `DUEDATE` | DATE |  |  |  |  |
| 23 | `TERMSOFPAYMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `TERMSOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 25 | `AMOUNTINDC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 26 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 27 | `CLEAREDAMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 28 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 29 | `AMOUNTINCC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 30 | `COMPANYCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 31 | `CLEAREDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 32 | `CUSTOMERREFERENCE` | CHAR(20) |  |  |  |  |
| 33 | `CUSTOMERREFERENCEDATE` | DATE |  |  |  |  |
| 34 | `VENDORREFERENCE` | CHAR(20) |  |  |  |  |
| 35 | `VENDORREFERENCEDATE` | DATE |  |  |  |  |
| 36 | `CARRYFORWARDFLAG` | SMALLINT | NOT NULL |  |  |  |
| 37 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 38 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 39 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 40 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 41 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 42 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 43 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 44 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 45 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 46 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 47 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 48 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 49 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINOPENDOCUMENTS.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.ABSVERSIONNUMBER,
       t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.FINANCIALYEARCOMPANYCODE,
       t.FINANCIALYEARCODE,
       t.DOCUMENTTEMPLATECOMPANYCODE,
       t.DOCUMENTTEMPLATECODE,
       t.STATISTICALGROUPCOMPANYCODE,
       t.STATISTICALGROUPCODE,
       t.DOCUMENTTYPECODE,
       t.CODE,
       t.LINENUMBER
FROM   DB2ADMIN.LOGFINOPENDOCUMENTS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
