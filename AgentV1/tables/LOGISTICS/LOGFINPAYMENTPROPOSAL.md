# DB2ADMIN.LOGFINPAYMENTPROPOSAL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 35
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 229965

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 3 | `DOCUMENTTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `DOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 5 | `PROPOSALDATE` | DATE | NOT NULL |  |  |  |
| 6 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 7 | `EXCHANGERATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 8 | `GLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `GLCODE` | CHAR(20) |  |  |  |  |
| 10 | `CHEQUELOTCODE` | CHAR(10) |  |  |  |  |
| 11 | `PROPOSALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `REFERENCETEXT1` | CHAR(20) |  |  |  |  |
| 13 | `CURRENTSTATUS` | INTEGER | NOT NULL |  |  |  |
| 14 | `COMPLETED` | SMALLINT | NOT NULL |  |  |  |
| 15 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 16 | `FIRSTLEVELAPPROVALDATE` | DATE |  |  |  |  |
| 17 | `FIRSTLEVELAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 18 | `SECONDLEVELAPPROVALDATE` | DATE |  |  |  |  |
| 19 | `SECONDLEVELAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 20 | `COMPLETEDDATE` | DATE |  |  |  |  |
| 21 | `COMPLETEDUSER` | CHAR(50) |  |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 28 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 29 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 30 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 31 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 32 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 33 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 34 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINPAYMENTPROPOSAL.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGFINPAYMENTPROPOSALLINE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.BUSINESSUNITCODE,
       t.DOCUMENTTEMPLATECOMPANYCODE,
       t.DOCUMENTTEMPLATECODE,
       t.PROPOSALDATE,
       t.DOCUMENTCURRENCYCODE,
       t.EXCHANGERATE,
       t.GLCOMPANYCODE,
       t.GLCODE,
       t.CHEQUELOTCODE,
       t.PROPOSALAMOUNT
FROM   DB2ADMIN.LOGFINPAYMENTPROPOSAL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
