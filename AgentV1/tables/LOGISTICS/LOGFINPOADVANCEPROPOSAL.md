# DB2ADMIN.LOGFINPOADVANCEPROPOSAL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 54
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 227498

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `FINYEARCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 3 | `FINYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 4 | `TYPE` | CHAR(1) |  |  |  |  |
| 5 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 6 | `ADUGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 7 | `ADUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 8 | `ADCODE` | CHAR(10) |  |  |  |  |
| 9 | `DOCUMENTTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 10 | `DOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 11 | `TRANSACTIONDATE` | DATE | NOT NULL |  |  |  |
| 12 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 13 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 14 | `ORDERPARTNERTYPE` | CHAR(1) |  |  |  |  |
| 15 | `ORDERPARTNERCODE` | CHAR(8) |  |  |  |  |
| 16 | `GLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 17 | `GLCODE` | CHAR(20) |  |  |  |  |
| 18 | `CHEQUELOTCODE` | CHAR(10) |  |  |  |  |
| 19 | `TRANSACTIONAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 20 | `REFERENCETEXT1` | CHAR(20) |  |  |  |  |
| 21 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 23 | `CURRENTSTATUS` | INTEGER | NOT NULL |  |  |  |
| 24 | `COMPLETED` | SMALLINT | NOT NULL |  |  |  |
| 25 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 26 | `FIRSTLEVELAPPROVALDATE` | DATE |  |  |  |  |
| 27 | `FIRSTLEVELAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 28 | `SECONDLEVELAPPROVALDATE` | DATE |  |  |  |  |
| 29 | `SECONDLEVELAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 30 | `COMPLETEDDATE` | DATE |  |  |  |  |
| 31 | `COMPLETEDUSER` | CHAR(50) |  |  |  |  |
| 32 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 33 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 34 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 35 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 36 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
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
| 50 | `CUSTOMERREFERENCE` | CHAR(20) |  |  |  |  |
| 51 | `CUSTOMERREFERENCEDATE` | DATE |  |  |  |  |
| 52 | `VENDORREFERENCE` | CHAR(20) |  |  |  |  |
| 53 | `VENDORREFERENCEDATE` | DATE |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINPOADVANCEPROPOSAL.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGFINPOADVANCEPROPOSALLINE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.FINYEARCOMPANYCODE,
       t.FINYEARCODE,
       t.TYPE,
       t.BUSINESSUNITCODE,
       t.ADUGENGROUPTYPECOMPANYCODE,
       t.ADUSERGENERICGROUPTYPECODE,
       t.ADCODE,
       t.DOCUMENTTEMPLATECOMPANYCODE,
       t.DOCUMENTTEMPLATECODE,
       t.TRANSACTIONDATE
FROM   DB2ADMIN.LOGFINPOADVANCEPROPOSAL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
