# DB2ADMIN.LOGFININTERUNITTRANSACTION

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 61
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 229274

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `BUPAYMENT` | SMALLINT | NOT NULL |  |  |  |
| 3 | `BUCLEARING` | SMALLINT | NOT NULL |  |  |  |
| 4 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 5 | `DOCUMENTTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `DOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `JVDOCUMENTTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `JVDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 9 | `TRANSACTIONDATE` | DATE | NOT NULL |  |  |  |
| 10 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 11 | `EXCHANGERATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 12 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 14 | `GLCODE` | CHAR(20) |  |  |  |  |
| 15 | `CHEQUELOTCODE` | CHAR(10) |  |  |  |  |
| 16 | `FODBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 17 | `FODFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 18 | `FODDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 19 | `FODSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 20 | `FODCODE` | CHAR(15) |  |  |  |  |
| 21 | `FODLINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 22 | `TRANSACTIONAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 23 | `REFERENCETEXT1` | CHAR(20) |  |  |  |  |
| 24 | `CURRENTSTATUS` | INTEGER | NOT NULL |  |  |  |
| 25 | `COMPLETED` | SMALLINT | NOT NULL |  |  |  |
| 26 | `EARLYPAYMENT` | CHAR(1) |  |  |  |  |
| 27 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 28 | `FIRSTLEVELAPPROVALDATE` | DATE |  |  |  |  |
| 29 | `FIRSTLEVELAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 30 | `SECONDLEVELAPPROVALDATE` | DATE |  |  |  |  |
| 31 | `SECONDLEVELAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 32 | `COMPLETEDDATE` | DATE |  |  |  |  |
| 33 | `COMPLETEDUSER` | CHAR(50) |  |  |  |  |
| 34 | `ADVCONTRADOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 35 | `ADVCONTRADOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 36 | `ADVCONTRADOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 37 | `ADVCONTRADOCSTCGROUPCODE` | CHAR(6) |  |  |  |  |
| 38 | `ADVCONTRADOCCODE` | CHAR(15) |  |  |  |  |
| 39 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 40 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 41 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 42 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 43 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 44 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 45 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 46 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 47 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 48 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 49 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 50 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 51 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 52 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 53 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 54 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 55 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 56 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 57 | `CUSTOMERREFERENCE` | CHAR(20) |  |  |  |  |
| 58 | `CUSTOMERREFERENCEDATE` | DATE |  |  |  |  |
| 59 | `VENDORREFERENCE` | CHAR(20) |  |  |  |  |
| 60 | `VENDORREFERENCEDATE` | DATE |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFININTERUNITTRANSACTION.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.BUPAYMENT,
       t.BUCLEARING,
       t.BUSINESSUNITCODE,
       t.DOCUMENTTEMPLATECOMPANYCODE,
       t.DOCUMENTTEMPLATECODE,
       t.JVDOCUMENTTEMPLATECOMPANYCODE,
       t.JVDOCUMENTTEMPLATECODE,
       t.TRANSACTIONDATE,
       t.DOCUMENTCURRENCYCODE,
       t.EXCHANGERATE
FROM   DB2ADMIN.LOGFININTERUNITTRANSACTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
