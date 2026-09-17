# DB2ADMIN.ABSLINKEDSPOOLFILE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `child_of_implicit_parent`
- **Columns**: 62
- **Primary key**: `COMPANYCODE`, `FATHERID`, `SPOOLABSOUTQUEUENAME`, `SPOOLSPOOLID`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 60940

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `FATHERID` | BIGINT | NOT NULL | PK | primary_key implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 3 | `SPOOLABSOUTQUEUENAME` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `SPOOLSPOOLID` | BIGINT | NOT NULL | PK | primary_key |  |
| 5 | `TYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `REPORTID` | CHAR(50) |  |  |  |  |
| 7 | `USERDESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 8 | `MDSTRING18` | VARCHAR(200) |  |  |  |  |
| 9 | `SEARCHKEY` | VARCHAR(500) |  |  |  |  |
| 10 | `CONTENTTYPE` | INTEGER | NOT NULL |  |  |  |
| 11 | `SENTBYMAIL` | SMALLINT | NOT NULL |  |  |  |
| 12 | `MAILBOXMAILIDENTIFIER` | BIGINT | NOT NULL |  |  |  |
| 13 | `EXPORTSTATUS` | INTEGER | NOT NULL |  |  |  |
| 14 | `EXPORTLOCATION` | VARCHAR(250) |  |  |  |  |
| 15 | `MDSTRING01` | VARCHAR(200) |  |  |  |  |
| 16 | `MDSTRING02` | VARCHAR(200) |  |  |  |  |
| 17 | `MDSTRING03` | VARCHAR(200) |  |  |  |  |
| 18 | `MDSTRING04` | VARCHAR(200) |  |  |  |  |
| 19 | `MDSTRING05` | VARCHAR(200) |  |  |  |  |
| 20 | `MDSTRING06` | VARCHAR(200) |  |  |  |  |
| 21 | `MDSTRING07` | VARCHAR(200) |  |  |  |  |
| 22 | `MDSTRING08` | VARCHAR(200) |  |  |  |  |
| 23 | `MDSTRING09` | VARCHAR(200) |  |  |  |  |
| 24 | `MDSTRING10` | VARCHAR(200) |  |  |  |  |
| 25 | `MDSTRING11` | VARCHAR(200) |  |  |  |  |
| 26 | `MDSTRING12` | VARCHAR(200) |  |  |  |  |
| 27 | `MDSTRING13` | VARCHAR(200) |  |  |  |  |
| 28 | `MDSTRING14` | VARCHAR(200) |  |  |  |  |
| 29 | `MDSTRING15` | VARCHAR(200) |  |  |  |  |
| 30 | `MDSTRING16` | VARCHAR(200) |  |  |  |  |
| 31 | `MDSTRING17` | VARCHAR(200) |  |  |  |  |
| 32 | `MDSTRING19` | VARCHAR(200) |  |  |  |  |
| 33 | `MDSTRING20` | VARCHAR(200) |  |  |  |  |
| 34 | `MDDATE01` | DATE |  |  |  |  |
| 35 | `MDDATE02` | DATE |  |  |  |  |
| 36 | `MDDATE03` | DATE |  |  |  |  |
| 37 | `MDDATE04` | DATE |  |  |  |  |
| 38 | `MDDATE05` | DATE |  |  |  |  |
| 39 | `MDNUMBER01` | DECIMAL(15,5) |  |  |  |  |
| 40 | `MDNUMBER02` | DECIMAL(15,5) |  |  |  |  |
| 41 | `MDNUMBER03` | DECIMAL(15,5) |  |  |  |  |
| 42 | `MDNUMBER04` | DECIMAL(15,5) |  |  |  |  |
| 43 | `MDNUMBER05` | DECIMAL(15,5) |  |  |  |  |
| 44 | `MDBOOLEAN01` | SMALLINT | NOT NULL |  |  |  |
| 45 | `MDBOOLEAN02` | SMALLINT | NOT NULL |  |  |  |
| 46 | `MDBOOLEAN03` | SMALLINT | NOT NULL |  |  |  |
| 47 | `MDBOOLEAN04` | SMALLINT | NOT NULL |  |  |  |
| 48 | `MDBOOLEAN05` | SMALLINT | NOT NULL |  |  |  |
| 49 | `MDMETADATAINFOS` | CLOB(1000000) |  |  |  |  |
| 50 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 51 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 52 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 53 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 54 | `ADDITIONALMAILS` | CHAR(90) |  |  |  |  |
| 55 | `OWNERCLASSNAME` | CHAR(50) |  |  |  |  |
| 56 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 57 | `DESTINATIONFOLDER` | VARCHAR(250) |  |  |  |  |
| 58 | `FILENAME` | VARCHAR(100) |  |  |  |  |
| 59 | `ANNULLED` | SMALLINT | NOT NULL |  |  |  |
| 60 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 61 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSLINKEDSPOOLFILETYPE_TYPE` | `TYPECODE` | [`ABSLINKEDSPOOLFILETYPE`](../PLATFORM/ABSLINKEDSPOOLFILETYPE.md) | `CODE` | RESTRICT | `ABSLINKEDSPOOLFILE.TYPECODE = ABSLINKEDSPOOLFILETYPE.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ABSLINKEDSPOOLFILE.COMPANYCODE = DIVISION.COMPANYCODE AND ABSLINKEDSPOOLFILE.DIVISIONCODE = DIVISION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `ABSLINKEDSPOOLFILE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `ABSLINKEDSPOOLFILEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.FATHERID,
       t.SPOOLABSOUTQUEUENAME,
       t.SPOOLSPOOLID,
       t.TYPECODE,
       t.REPORTID,
       t.USERDESCRIPTION,
       t.MDSTRING18,
       t.SEARCHKEY,
       t.CONTENTTYPE,
       t.SENTBYMAIL
FROM   DB2ADMIN.ABSLINKEDSPOOLFILE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
